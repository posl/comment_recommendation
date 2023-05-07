def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(K+1, N+1)):
        for j in range(min(K-i+1, N-i+1)):
            tmp = 0
            tmpV = []
            for k in range(i):
                tmp += V[k]
                tmpV.append(V[k])
            for k in range(j):
                tmp += V[N-1-k]
                tmpV.append(V[N-1-k])
            tmpV.sort()
            for k in range(K-i-j):
                if tmpV[k] >= 0:
                    break
                tmp -= tmpV[k]
            ans = max(ans, tmp)
    print(ans)
