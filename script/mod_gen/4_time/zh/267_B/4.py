def isSplit(S):
    if S[0] == '0':
        return False
    else:
        for i in range(1, 10):
            if S[i] == '0':
                return True
        return False

if __name__ == '__main__':
    isSplit()