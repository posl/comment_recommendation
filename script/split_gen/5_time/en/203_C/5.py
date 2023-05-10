def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    for a, b in AB:
        if K < a:
            break
        K += b
    print(K)
