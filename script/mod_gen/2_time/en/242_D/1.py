def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        if t % 3 == 0:
            if k % 3 == 1:
                print(S[0])
            elif k % 3 == 2:
                print(S[1])
            else:
                print(S[2])
        elif t % 3 == 1:
            if k % 3 == 1:
                print(S[1])
            elif k % 3 == 2:
                print(S[2])
            else:
                print(S[0])
        else:
            if k % 3 == 1:
                print(S[2])
            elif k % 3 == 2:
                print(S[0])
            else:
                print(S[1])

if __name__ == '__main__':
    main()