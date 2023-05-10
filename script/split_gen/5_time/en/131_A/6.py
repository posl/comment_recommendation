def check_security_code(code):
    if code[0] == code[1] and code[1] == code[2]:
        return False
    elif code[1] == code[2] and code[2] == code[3]:
        return False
    else:
        return True
