def main():
    N, Q = map(int, input().split())
    S = input()
    AC_count = [0] * (N+1)
    for i in range(N):
        if S[i:i+2] == 'AC':
            AC_count[i+1] = AC_count[i] + 1
        else:
            AC_count[i+1] = AC_count[i]
    for i in range(Q):
        l, r = map(int, input().split())
        print(AC_count[r-1] - AC_count[l-1])

if __name__ == '__main__':
    main()