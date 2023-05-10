def check_security_code(security_code):
    if security_code[0] == security_code[1]:
        if security_code[1] == security_code[2]:
            return "Bad"
        else:
            if security_code[2] == security_code[3]:
                return "Bad"
    elif security_code[1] == security_code[2]:
        if security_code[2] == security_code[3]:
            return "Bad"
    return "Good"
