def main():
    N, M = map(int, input().split())
    store = [list(map(int, input().split())) for _ in range(N)]
    store.sort()
    ans = 0
    for i in range(N):
        if M > store[i][1]:
            ans += store[i][0] * store[i][1]
            M -= store[i][1]
        else:
            ans += store[i][0] * M
            break
    print(ans)
