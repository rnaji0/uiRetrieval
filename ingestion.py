import re
import os
from typing import List, Dict
from bs4 import BeautifulSoup
import tiktoken

encoding = tiktoken.encoding_for_model("text-embedding-3-small")


def extractTemplate(vue_content: str) -> str:

    match = re.search(r"<template>(.*?)</template>", vue_content, re.DOTALL)
    return match.group(1).strip() if match else ""


def parseTemplate(templateStr: str):
    soup = BeautifulSoup(templateStr, "html.parser")
    return soup


def parseVueFile(filepath: str) -> List[Dict]:
    with open(filepath, "r", encoding="utf-8") as f:
        vueContent = f.read()

    templateStr = extractTemplate(vueContent)
    astRoot = parseTemplate(templateStr)
    
    return astRoot


def chunk_by_tokens(snippet: str, max_tokens: int = 500):
    tokens = encoding.encode(snippet)
    chunks = []

    for i in range(0, len(tokens), max_tokens):
        token_chunk = tokens[i:i+max_tokens]
        sub_snippet = encoding.decode(token_chunk)
        chunks.append(sub_snippet)

    return chunks

print(parseVueFile("storage/components/ContactUs.vue"))

