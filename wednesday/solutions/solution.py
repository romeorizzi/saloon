

original_string = None
encoded_string = None

def get_original_string(string_length, string_over_alphabet_0123456789comma):
    nonlocal encoding_string
    seq_of_positive_naturals = []
    next_val = 0
    for char in string_over_alphabet_0123456789comma:
        if char != -1:
            next_val = 10*next_val + char
        else:
            seq_of_positive_naturals.append(next_val)
            next_val = 0
    seq_of_positive_naturals.append(next_val)
    next_val = 0

            
def tell_encoded_string_length():
    return len(encoded_string)

def tell_encoded_string_ith_char(i):
    return encoded_string(i)

def get_encoded_string(string_length, string_over_reduced_alphabet):
    nonlocal original_string
    original_string = string_over_reduced_alphabet[:]

def tell_original_string_length():
    return len(original_string)

def tell_original_string_ith_char(i):
    return original_string(i)

