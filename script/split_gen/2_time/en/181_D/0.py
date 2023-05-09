def main():
    S = input()
    if len(S) == 1:
        if int(S) % 8 == 0:
            print('Yes')
        else:
            print('No')
    elif len(S) == 2:
        if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
    else:
        S = list(S)
        S.sort()
        for i in range(100, 1000, 8):
            if str(i).count('0') == 2:
                continue
            if str(i)[0] in S:
                if str(i)[1] in S:
                    if str(i)[2] in S:
                        print('Yes')
                        return
        print('No')
