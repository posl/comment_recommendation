def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    result = 0
    for i in range(min(N, K)+1):
        for j in range(min(N, K)-i+1):
            jewels = V[:i] + V[N-j:]
            jewels.sort()
            for k in range(min(len(jewels), K-i-j)):
                if jewels[k] < 0:
                    jewels[k] = 0
            result = max(result, sum(jewels))
    print(result)
