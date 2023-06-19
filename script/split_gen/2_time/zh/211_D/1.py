def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    for i in range(M):
        if AB[i][0] == 1:
            ans += 1
        if AB[i][1] == N:
            break
    print(ans)
