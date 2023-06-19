def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    dic = {}
    for i in range(N + 1):
        if S[i] % M in dic:
            dic[S[i] % M] += 1
        else:
            dic[S[i] % M] = 1
    ans = 0
    for i in dic:
        ans += dic[i] * (dic[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()