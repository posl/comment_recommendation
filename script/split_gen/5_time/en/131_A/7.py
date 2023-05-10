def check_security_code(input):
    input = str(input)
    if input[0] == input[1] or input[1] == input[2] or input[2] == input[3]:
        print("Bad")
    else:
        print("Good")
