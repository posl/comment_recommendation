def check(S):
    if len(S) == 1:
        if S == '8':
            return True
        else:
            return False
    elif len(S) == 2:
        if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
            return True
        else:
            return False
    else:
        for i in range(100, 1000):
            if i % 8 == 0:
                if S.count(str(i)[0]) >= 1 and S.count(str(i)[1]) >= 1 and S.count(str(i)[2]) >= 1:
                    return True
        return False

if __name__ == '__main__':
    check()