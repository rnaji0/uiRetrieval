<template>
  <Transition name="slide-fade">
    <div v-show="isVisible" class="relative h-fit rounded [&>*]:transition-all [&>*]:duration-300 [&>*]:ease-in-out order-2">
      <div class="w-full h-full bg-[var(--primary-color)] group-hover:bg-[#323232] top-[3px] absolute block rounded-[2rem]"></div>
      <div class="flex h-full flex-col min-w-full relative rounded-[1.75rem] group-hover:brightness-[0.98] overflow-hidden bg-[#fcfcff] border-[1px] p-6">
        <h2 class="text-[1.15rem] font-bold mb-4">Contact Us</h2>
        <div class="flex flex-col gap-2.5">
          <NuxtLink v-for="contact in modelValue" :key="contact.url"
            :to="contact.url" target="_blank" 
            class="group relative flex items-center gap-x-3 px-2 py-2.5 transition-all duration-300 w-full bg-[var(--primary-color)]/[0.03] rounded-xl hover:bg-[var(--primary-color)]/[0.06]">
            <div class="flex-shrink-0">
              <div class="bg-gradient-to-b from-[var(--primary-color)]/[0.08] to-[var(--primary-color)]/[0.12] rounded-lg p-2 flex items-center justify-center">
                <Icon :name="contact.icon" class="text-[1.2rem] text-[var(--primary-color)]" />
              </div>
            </div>
            <div class="flex flex-col gap-0.5">
              <div class="flex items-center gap-1.5">
                <span class="text-[0.825rem] font-semibold text-gray-900">{{ contact.title }}</span>
                <Icon v-if="contact.verified" name="material-symbols:verified-outline" class="text-[0.9rem] text-[var(--primary-color)]" />
                <span v-if="contact.badge" class="text-[0.7rem] font-medium text-[var(--primary-color)] bg-[var(--primary-color)]/10 px-1.5 py-0.5 rounded">{{ contact.badge }}</span>
              </div>
              <span class="text-[0.75rem] text-gray-500">{{ contact.subtitle }}</span>
            </div>
            <div class="absolute right-2 top-[55%] -translate-y-1/2 opacity-0 -translate-x-1 group-hover:opacity-100 group-hover:translate-x-0 transition-all duration-300">
              <Icon name="material-symbols:arrow-outward" class="text-[1.1rem] text-[var(--primary-color)]" />
            </div>
          </NuxtLink>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
const props = defineProps({
  modelValue: {
    type: Array,
    required: true
  },
  isVisible: {
    type: Boolean,
    default: true
  }
})
</script> 
