def main():
    N = int(input())
    S = input()
    Q = int(input())
    for i in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            S = S[:A-1] + S[B-1] + S[A:B-1] + S[A-1] + S[B:]
        else:
            S = S[N:] + S[:N]
    print(S)

if __name__ == '__main__':
    main()