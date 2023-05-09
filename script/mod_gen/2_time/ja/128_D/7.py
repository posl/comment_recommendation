def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(N+1):
        for j in range(N-i+1):
            if i+j > K:
                break
            tmp = V[:i] + V[N-j:]
            tmp.sort()
            for k in range(K-(i+j)):
                if k >= len(tmp) or tmp[k] >= 0:
                    break
                tmp[k] = 0
            ans = max(ans, sum(tmp))
    print(ans)

if __name__ == '__main__':
    main()