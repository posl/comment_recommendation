def find_error_number(n,s):
    error_number = 0
    for i in range(n):
        for a in range(1,1000):
            for b in range(1,1000):
                if s[i] == 4*a*b+3*a+3*b:
                    break
                if a == 999 and b == 999:
                    error_number += 1
    return error_number

if __name__ == '__main__':
    find_error_number()