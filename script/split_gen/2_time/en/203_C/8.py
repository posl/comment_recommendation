def main():
    N, K = map(int, input().split())
    friend = [list(map(int, input().split())) for _ in range(N)]
    friend.sort()
    for f in friend:
        if K >= f[0]:
            K += f[1]
    print(K)
