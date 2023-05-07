def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    for i in range(N):
        T[i] = [T[i], i]
    T.sort()
    ans = [0] * N
    for t, i in T:
        ans[i] = t + S[i]
        S[(i+1)%N] = min(S[(i+1)%N], S[i])
    print(*ans, sep='
')

if __name__ == '__main__':
    main()