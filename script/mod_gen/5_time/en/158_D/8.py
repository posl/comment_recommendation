def main():
    S = input()
    Q = int(input())
    r = False
    for _ in range(Q):
        T, *args = input().split()
        if T == '1':
            r = not r
        else:
            F, C = args
            if F == '1':
                if r:
                    S = S + C
                else:
                    S = C + S
            else:
                if r:
                    S = C + S
                else:
                    S = S + C
    if r:
        S = S[::-1]
    print(S)

if __name__ == '__main__':
    main()