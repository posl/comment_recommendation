def isSplit(s):
    if s[0] == '1':
        return False
    for i in range(1, len(s)-1):
        if s[i] == '1':
            if s[i-1] == '0' and s[i+1] == '0':
                return True
    return False
s = input()

if __name__ == '__main__':
    isSplit()