def main():
    N, K = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(N)]
    ab.sort()
    for a, b in ab:
        if a > K:
            break
        K += b
    print(K)
