def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x:x[1])
    AB.sort(key=lambda x:x[0], reverse=True)
    # print(AB)
    ans = []
    for i in range(N):
        ans.append([i+1, i+1])
    for i in range(M):
        ans[AB[i][0]-1][1] = AB[i][1]
    ans.sort(key=lambda x:x[1])
    # print(ans)
    for i in range(N-1):
        if ans[i][0] > ans[i+1][0]:
            print(-1)
            return
    for i in range(N):
        print(ans[i][0], end=" ")
    print()
