def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    cumsum = [0]
    for i in range(N):
        cumsum.append(cumsum[i] + A[i])
    dic = {}
    for i in range(N+1):
        if cumsum[i] - K in dic:
            ans += dic[cumsum[i]-K]
        if cumsum[i] in dic:
            dic[cumsum[i]] += 1
        else:
            dic[cumsum[i]] = 1
    print(ans)

if __name__ == '__main__':
    main()