def main():
    N, M = map(int, input().split())
    stores = []
    for _ in range(N):
        A, B = map(int, input().split())
        stores.append((A, B))
    stores.sort()
    ans = 0
    for A, B in stores:
        if M <= B:
            ans += A * M
            break
        else:
            ans += A * B
            M -= B
    print(ans)
