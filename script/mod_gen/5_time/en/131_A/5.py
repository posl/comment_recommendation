def check_security_code(code):
    if code[0] == code[1] or code[1] == code[2] or code[2] == code[3]:
        print('Bad')
    else:
        print('Good')

if __name__ == '__main__':
    check_security_code()