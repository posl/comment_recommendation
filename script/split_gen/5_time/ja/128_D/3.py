def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(N, K) + 1):
        for r in range(min(N, K) - l + 1):
            if l + r > N:
                continue
            if l + r > K:
                continue
            if l + r == 0:
                continue
            V2 = sorted(V[:l] + V[N-r:])
            #print(V2)
            tmp = sum(V2)
            for i in range(min(K-l-r, len(V2))):
                if V2[i] < 0:
                    tmp -= V2[i]
                else:
                    break
            ans = max(ans, tmp)
    print(ans)
