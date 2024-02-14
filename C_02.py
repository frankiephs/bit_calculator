def statement_generator(statement, decoration):
    print(f"{decoration * 5} {statement} {decoration * 5}")


def instructions():
    statement_generator("Instructions","-")

    print('''
- Instructions 1
- Instructions 2
- etc
      ''')

want_instructions = input("Press <enter> to read or any key to continue: ")



if want_instructions == "":
    instructions()