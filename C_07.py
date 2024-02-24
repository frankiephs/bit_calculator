
def int_check(question, low):


    error = "please enter a number that is more than zero\n"
    while True:
        try:
            response = int(input(question))

            if response >= 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

def integer_calc():
    integer = int_check("integer: ", 0)

    raw_binary = bin(integer)

    # removing the leading 0b in the front
    binary = raw_binary[2:]
    num_bits = len(binary)

    answer = f"{integer} in binary is {binary}. we need {num_bits} to represent it"

    return answer

integer_ans = integer_calc()
print(integer_ans)