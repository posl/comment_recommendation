def check(S):
    if len(S) == 1:
        if int(S) % 8 == 0:
            return True
        else:
            return False
    elif len(S) == 2:
        if int(S) % 8 == 0:
            return True
        elif int(S[1] + S[0]) % 8 == 0:
            return True
        else:
            return False
    else:
        for i in range(104, 1000, 8):
            if all(S.count(str(j)) >= str(i).count(str(j)) for j in range(10)):
                return True
        return False

if __name__ == '__main__':
    check()