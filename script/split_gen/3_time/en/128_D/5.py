def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    result = 0
    for i in range(1, min(N, K)+1):
        for j in range(i+1):
            jewels = V[:j] + V[N-(i-j):]
            jewels.sort()
            for k in range(min(K-i, len(jewels))):
                if jewels[k] < 0:
                    jewels[k] = 0
            result = max(result, sum(jewels))
    print(result)
