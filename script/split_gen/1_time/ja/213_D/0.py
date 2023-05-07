def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    for i in range(N):
        G[i].sort()
    ans = [0]
    used = [0]*N
    used[0] = 1
    now = 0
    while True:
        for i in G[now]:
            if used[i] == 0:
                ans.append(i+1)
                used[i] = 1
                now = i
                break
        else:
            if now == 0:
                break
            else:
                ans.append(now+1)
                now = ans[-3]
    print(*ans)
