def main():
    N, Q = map(int, input().split())
    S = input()
    AC = [0] * (N + 1)
    for i in range(1, N):
        if S[i-1] == "A" and S[i] == "C":
            AC[i] = AC[i-1] + 1
        else:
            AC[i] = AC[i-1]
    for _ in range(Q):
        l, r = map(int, input().split())
        print(AC[r-1] - AC[l-1])

if __name__ == '__main__':
    main()