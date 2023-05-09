def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    for a, b in AB:
        if K >= a:
            K += b
        else:
            break
    print(K)
