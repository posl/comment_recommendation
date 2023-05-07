def isSplit(s):
    if s[0] != '0':
        return False
    else:
        for i in range(1, 10):
            if s[i] == '1':
                for j in range(i+1, 10):
                    if s[j] == '1':
                        for k in range(i, j+1):
                            if s[k] == '0':
                                return True
    return False
s = input()

if __name__ == '__main__':
    isSplit()