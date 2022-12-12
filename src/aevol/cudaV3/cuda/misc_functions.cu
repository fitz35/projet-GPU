//
// Created by elturpin on 16/11/2020.
//
#include "misc_functions.cuh"

#include "aevol_constants.h"


__device__ is_smth compute_is_smth (const char* sequence) {
  is_smth smth;
  smth.is_terminator = true;
  smth.is_prot_start = true;
  uint8_t distance = 0;
  int left, right;

  for(left = 0, right = TERM_SIZE - 1; left < MAXE_SIZE;  ++left, --right) {
    // is_promoter
    if (left < PROM_SIZE && sequence[left] != PROM_SEQ[left]){
      distance++;
      if (distance > PROM_MAX_DIFF)
        smth.is_promoter = 0b1111;
    }
    // is_terminator
    if (left < TERM_STEM_SIZE && sequence[left] == sequence[right])
      smth.is_terminator = false;
    
    // is_prot_start
    if (left < SHINE_DAL_SIZE && sequence[left] != SHINE_DAL_SEQ[left])
      smth.is_prot_start = false;

    if (left < CODON_SIZE && sequence[left + SHINE_DAL_SIZE + SD_START_SPACER] != '0')
      smth.is_prot_start = false;
    
  }

  
  return smth;
}

__device__ uint8_t is_promoter(const char* sequence) {
  uint8_t distance = 0;
  for (int offset = 0; offset < PROM_SIZE; ++offset) {
    if (sequence[offset] != PROM_SEQ[offset]){
      distance++;
      if (distance > PROM_MAX_DIFF)
        return 0b1111;
    }
  }
  return distance;
}

__device__ bool is_terminator(const char* sequence) {
  int left, right;
  for (left = 0, right = TERM_SIZE - 1; left < TERM_STEM_SIZE; ++left, --right) {
    if (sequence[left] == sequence[right])
      return false;
  }
  return true;
}

__device__ bool is_prot_start(const char* sequence) {
  for (int offset = 0; offset < SHINE_DAL_SIZE; ++offset) {
    if (sequence[offset] != SHINE_DAL_SEQ[offset])
      return false;
  }
  for (int offset = 0; offset < CODON_SIZE; ++offset) {
    if (sequence[offset + SHINE_DAL_SIZE + SD_START_SPACER] != '0')
      return false;
  }
  return true;
}

__device__ uint8_t translate_to_codon(const char* seq) {
  uint8_t codon = 0;

  for (uint8_t i = 0; i < CODON_SIZE; ++i) {
    codon += (seq[i] - '0') << (CODON_SIZE - 1 - i);
  }

  return codon;
}
