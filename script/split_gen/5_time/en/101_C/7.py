def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = 0
    for i in range(1, N):
        if (N - i) % (K - 1) == 1:
            result += 1
    print(result)
