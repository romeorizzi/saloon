#include<cassert>

int rank(int integer_to_be_encoded) {
  if(integer_to_be_encoded >= 0)
    return 2*integer_to_be_encoded;
  else
    return 2*(-integer_to_be_encoded) -1;    
}
int unrank(int position_in_the_list) {
  assert( position_in_the_list >= 0); 
  if(position_in_the_list % 2 == 0)
    return position_in_the_list/2;
  else
    return -(position_in_the_list+1)/2;    
}
