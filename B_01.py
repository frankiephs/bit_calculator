def statement_generator(statement, decoration):
    print(f"{decoration * 5} {statement} {decoration * 5}")


def instructions():
    statement_generator("Instructions","-")
    print('''
- Instructions 1
- Instructions 2
- etc
      ''')



def get_filetype():


    while True:
        response = input("File type: ").lower()

        if response == "xxx" or response == "i":
            return response

        elif response in ['integer', 'int']:
            return "integer"
        
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        elif response in ['text', 'txt', 't']:
            return "text"
        
        else:
            print("Please enter a valid file type")



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

def image_calc():
    width = int_check("width: ", 1)
    height = int_check("height: ", 1)

    num_pixels = width * height
    num_bits = num_pixels * 24

    answer = (f"number of pixels: {width} x {height} = {num_pixels}" 
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer


def integer_calc():
    integer = int_check("integer: ", 0)

    raw_binary = bin(integer)

    # removing the leading 0b in the front
    binary = raw_binary[2:]
    num_bits = len(binary)

    answer = f"{integer} in binary is {binary}. we need {num_bits} to represent it"

    return answer


def calc_text_bits():
    response = input("Enter some text...")

    num_chars = len(response)
    num_bits = num_chars * 8

    answer = (f"{response} has {num_chars} characters." 
            f"\nWe need {num_chars} x 8 bits to represent it"
            f"\nwhich is {num_bits} bits")
    
    return answer





want_instructions = input("Press <enter> to read or any key to continue: ")



if want_instructions == "":
    instructions()



while True:
    file_type = get_filetype()

    if file_type == "xxx":
        break
    

    if file_type == 'i':

        want_image = input("Press enter for int or key for img")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"
        
        
    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)