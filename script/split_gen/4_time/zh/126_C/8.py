def main():
    N, K = map(int, input().split())
    total = 0
    for i in range(1, N + 1):
        if i >= K:
            total += 1
        else:
            total += 1 / 2 ** (len(bin(K - 1)) - 2)
    print(total / N)
