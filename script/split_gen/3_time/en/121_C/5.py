def main():
    N, M = map(int, input().split())
    stores = []
    for i in range(N):
        A, B = map(int, input().split())
        stores.append((A, B))
    stores.sort()
    ans = 0
    for i in range(N):
        if M > stores[i][1]:
            ans += stores[i][0] * stores[i][1]
            M -= stores[i][1]
        else:
            ans += stores[i][0] * M
            break
    print(ans)
main()
