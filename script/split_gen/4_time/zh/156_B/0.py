def main():
    N, K = map(int, input().split())
    i = 1
    while N >= K:
        N //= K
        i += 1
    print(i)
