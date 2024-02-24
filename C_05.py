def calc_text_bits():
    response = input("Enter some text...")

    num_chars = len(response)
    num_bits = num_chars * 8

    answer = (f"{response} has {num_chars} characters." 
            f"\nWe need {num_chars} x 8 bits to represent it"
            f"\nwhich is {num_bits} bits")
    
    return answer




text_ans = calc_text_bits()
print(text_ans)
