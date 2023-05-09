def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    result = 0
    for i in range(N - K + 1):
        result = max(result, len(set(c[i:i + K])))
    print(result)
