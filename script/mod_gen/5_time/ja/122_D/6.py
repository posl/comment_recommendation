def check(s):
    for i in range(len(s)-2):
        if s[i:i+3] == "AGC":
            return False
    for i in range(len(s)-1):
        if s[i:i+2] == "AC":
            return False
    for i in range(len(s)-1):
        if s[i:i+2] == "GA":
            return False
    for i in range(len(s)-1):
        if s[i:i+2] == "CA":
            return False
    return True

if __name__ == '__main__':
    check()