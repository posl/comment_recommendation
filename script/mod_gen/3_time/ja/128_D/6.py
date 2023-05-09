def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(1, min(N, K)+1):
        for j in range(i+1):
            tmp = V[:j] + V[N-(i-j):]
            tmp.sort()
            s = sum(tmp)
            for k in range(min(K-i, i-j)):
                if tmp[k] >= 0:
                    break
                s -= tmp[k]
            ans = max(ans, s)
    print(ans)

if __name__ == '__main__':
    main()