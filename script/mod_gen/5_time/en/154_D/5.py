def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        tmp = 0
        for j in range(i, i+K):
            tmp += (p[j]+1)/2
        if tmp > ans:
            ans = tmp
    print(ans)

if __name__ == '__main__':
    main()