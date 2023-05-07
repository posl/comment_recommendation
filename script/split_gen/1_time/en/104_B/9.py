def check_problem104b(input):
    if input[0] != "A":
        return False
    if input[2:-1].count("C") != 1:
        return False
    for i in range(1,len(input)):
        if input[i] != "C" and input[i].isupper():
            return False
    return True
