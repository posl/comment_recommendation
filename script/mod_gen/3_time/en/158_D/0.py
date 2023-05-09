def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        T = input().split()
        if T[0] == '1':
            S = S[::-1]
        else:
            if T[1] == '1':
                S = T[2] + S
            else:
                S = S + T[2]
    print(S)

if __name__ == '__main__':
    main()