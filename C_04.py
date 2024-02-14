
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




for items in range(0,2):
    integer = int_check("integer: ", 0)
    print(integer)

print()

for items in range(0,2):
    width = int_check("width: ", 1)
    print(width)

print()

for items in range(0,2):
    height = int_check("height: ", 1)
    print(height)