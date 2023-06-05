def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    for A, B in AB:
        if K >= A:
            K += B
    print(K)
