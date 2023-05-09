def main():
    N = int(input())
    S = str(N)
    if len(S) == 1:
        if int(S) % 3 == 0:
            print(0)
        else:
            print(-1)
    else:
        Nsum = sum([int(i) for i in S])
        if Nsum % 3 == 0:
            print(0)
        else:
            if Nsum % 3 == 1:
                if S.count('1') > 0 or S.count('4') > 0 or S.count('7') > 0:
                    if len(S) == 2:
                        print(1)
                    else:
                        print(0)
                else:
                    if S.count('2') > 1 or S.count('5') > 1 or S.count('8') > 1:
                        print(2)
                    else:
                        print(-1)
            else:
                if S.count('2') > 0 or S.count('5') > 0 or S.count('8') > 0:
                    if len(S) == 2:
                        print(1)
                    else:
                        print(0)
                else:
                    if S.count('1') > 1 or S.count('4') > 1 or S.count('7') > 1:
                        print(2)
                    else:
                        print(-1)

if __name__ == '__main__':
    main()