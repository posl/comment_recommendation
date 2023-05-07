def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    right = 0
    for i in range(M):
        if right < AB[i][0]:
            ans += 1
            right = AB[i][1] - 1
    print(ans)
