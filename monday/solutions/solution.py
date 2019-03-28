

original_string = None
encoded_string = None

def get_original_string(string_length, string_over_alphabet_0123456789comma):
    global encoded_string
    encoded_string = string_over_alphabet_0123456789comma[:]
            
def tell_encoded_string_length():
    global encoded_string
    return len(encoded_string)

def tell_encoded_string_ith_char(i):
    global encoded_string
    return encoded_string[i]

def get_encoded_string(string_length, string_over_reduced_alphabet):
    global original_string
    original_string = string_over_reduced_alphabet[:]

def tell_original_string_length():
    global original_string
    return len(original_string)

def tell_original_string_ith_char(i):
    global original_string
    return original_string[i]

