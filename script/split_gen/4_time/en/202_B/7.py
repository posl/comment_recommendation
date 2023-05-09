def solve(string):
    result = ""
    for i in range(len(string)-1,-1,-1):
        if string[i] == "6":
            result += "9"
        elif string[i] == "9":
            result += "6"
        else:
            result += string[i]
    return result
