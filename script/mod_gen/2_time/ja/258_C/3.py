def main():
    N, Q = map(int, input().split())
    S = input()
    for i in range(Q):
        t, x = map(int, input().split())
        x -= 1
        if t == 1:
            S = S[N-1] + S[:N-1]
        else:
            print(S[x])

if __name__ == '__main__':
    main()