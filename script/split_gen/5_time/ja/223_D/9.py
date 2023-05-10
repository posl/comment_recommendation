def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    if M == 0:
        print(*[i for i in range(1, N+1)])
        return
    if N == 2:
        print(-1)
        return
    AB.sort(key=lambda x: x[1])
    AB.sort(key=lambda x: x[0])
    if AB[0][0] == 1:
        print(-1)
        return
    ans = [1, AB[0][0], AB[0][1]]
    for i in range(1, M):
        if AB[i][0] == ans[-1]:
            ans.append(AB[i][1])
        else:
            ans.append(AB[i][0])
    print(*ans)
