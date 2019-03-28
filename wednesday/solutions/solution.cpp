#include <vector>
#include <algorithm>
#include <cassert>
#include <limits>

using std::vector;

vector<int> original_string;
vector<int> encoded_string;

void get_original_string(int string_length, int string_over_alphabet_0123456789comma[]) {
  for(int i = 0; i < string_length; i++)
    encoded_string.push_back(string_over_alphabet_0123456789comma[i]);
}
            
int tell_encoded_string_length() {
  return encoded_string.size();
}

int tell_encoded_string_ith_char(int i) {
  return encoded_string[i];
}

void get_encoded_string(int string_length, int string_over_reduced_alphabet[]) {
  for(int i = 0; i < string_length; i++)
    original_string.push_back(string_over_reduced_alphabet[i]);
}

int tell_original_string_length() {
  return original_string.size();
}

int tell_original_string_ith_char(int i) {
  return original_string[i];
}
