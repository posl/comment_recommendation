def main():
    N, K = map(int, input().split())
    if N >= K:
        print(1.0)
        return
    result = 0.0
    for i in range(1, N + 1):
        if i >= K:
            result += 1.0
        else:
            n = 1
            while i * 2 ** n < K:
                n += 1
            result += 1.0 / (N * 2 ** (n - 1))
    print(result)
