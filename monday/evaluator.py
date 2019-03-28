import random

import turingarena as ta

allowed_keys = [-1,0,1,2,3,4,5,6,7,8,9]

def test_with_seq(seq):
    def turn_off_goals():
        ta.goals["correct"] = False
        ta.goals["correct_C_is_2"] = False
        ta.goals["correct_C_is_1"] = False
        
    encoded_seq = []
    decoded_seq = []
    try:
        with ta.run_algorithm(ta.submission.source) as process:
            process.procedures.get_original_string(len(seq), seq)
            encoded_len = process.functions.tell_encoded_string_length()
            for i in range(encoded_len):
                encoded_seq.append(process.functions.tell_encoded_string_ith_char(i))
    except ta.AlgorithmError as e:
        turn_off_goals()
        print(e)

    try:
        with ta.run_algorithm(ta.submission.source) as process:
            process.procedures.get_encoded_string(len(encoded_seq), encoded_seq)
            decoded_len = process.functions.tell_original_string_length()
            for i in range(decoded_len):
                decoded_seq.append(process.functions.tell_original_string_ith_char(i))
    except ta.AlgorithmError as e:
        turn_off_goals()
        print(e)

    print(f"The string to be encoded was:\n   {seq}")
    print(f"You encoded it with:\n   {encoded_seq}")
    all_allowed_keys = True
    wrong_key = None
    wrong_pos = None 
    for pos,val in zip(range(len(encoded_seq)), encoded_seq):
        if val not in allowed_keys:
            turn_off_goals()
            all_allowed_keys = False
            wrong_key = val
            wrong_pos = pos 
            break
    if not all_allowed_keys:
        print(f"NO: Use of key '{wrong_key}' forbidden in the encoded sequence. You used it in position {wrong_pos} (positions start from 0).")
    else:
        print("OK. You only used allowed keys. Good!")

    print(f"Which you decoded as:\n   {decoded_seq}")
    if len(decoded_seq) != len(seq):
        turn_off_goals()
        print(f"NO: Notice that the lengths of the original sequence (which contained {len(decoded_seq)} charactes over the alphabet {'0','1','2','3','4','5','6','7','8','9','-1'}) and the decoded one (which contains {len(seq)} numbers over the same alphabet {'0','1','2','3','4','5','6','7','8','9','-1'}) differ.")
    are_equal = True
    for i in range(len(seq)):
        if seq[i] != decoded_seq[i]:
            turn_off_goals()
            are_equal = False
            break
    if not are_equal:
        print(f"NO: The original sequence and the decoded one differ in position {i}, where the original reports a '{seq[i]}' character and the decoded reports a '{decoded_seq[i]}' character.")
    else:
        print("OK. You correctly reconstructed the original sequence. Congrats!")
    if len(seq) > 0:
        return (len(decoded_seq) - 3)/len(seq)
    else:
        return 1.0

def seq_in_eleven_keys_alphabet(seq_of_pos_nats):
    #print(seq_of_pos_nats)
    res = []
    for n in seq_of_pos_nats:
        n_encoded_in_reverse = []
        while n > 0:
            n_encoded_in_reverse.append(n%10)
            n -= n%10
            n //= 10
        for char in reversed(n_encoded_in_reverse):
            res.append(char)
        res.append(-1)
    #print(res)
    return res

C_min = 1.0
def test_and_update_C_min(test_case):
    global C_min
    lastC = test_with_seq(test_case)
    if lastC > C_min:
        C_min = lastC
    if C_min > 2.0:
        ta.goals["correct_C_is_2"] = False
    if C_min > 1.0:
        ta.goals["correct_C_is_1"] = False

test_and_update_C_min(test_case=seq_in_eleven_keys_alphabet(list(range(1,20))))
test_and_update_C_min(test_case=seq_in_eleven_keys_alphabet(list(range(5,100,10))))
    
ta.goals.setdefault("correct", True)
ta.goals.setdefault("correct_C_is_2", True)
ta.goals.setdefault("correct_C_is_1", True)
print(ta.goals)

