def check_security_code(security_code):
    if security_code[0] == security_code[1] == security_code[2] or security_code[1] == security_code[2] == security_code[3]:
        return "Bad"
    else:
        return "Good"

if __name__ == '__main__':
    check_security_code()