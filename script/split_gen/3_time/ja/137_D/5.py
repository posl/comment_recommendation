def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    que = []
    for i in range(1, M + 1):
        for a, b in AB:
            if a == i:
                que.append(b)
            else:
                break
        if que:
            ans += que.pop()
    print(ans)
