def main():
    N, L = map(int, input().split())
    print(sum(i for i in range(1, N) if L + i > 0) + sum(i for i in range(1, N) if L + i - 1 < 0))
