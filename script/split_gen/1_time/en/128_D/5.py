def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(K+1):
        for j in range(K-i+1):
            if i + j > N:
                continue
            tmp = V[:i] + V[N-j:]
            tmp.sort()
            for k in range(K-i-j):
                if len(tmp) <= k or tmp[k] >= 0:
                    break
                tmp[k] = 0
            ans = max(ans, sum(tmp))
    print(ans)
