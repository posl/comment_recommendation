def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = []
    for i in range(1, N+1):
        ans.append(i)
    for i in range(M-1, -1, -1):
        a = AB[i][0]
        b = AB[i][1]
        if ans.index(a) > ans.index(b):
            ans.remove(a)
            ans.insert(ans.index(b), a)
    if len(set(ans)) == N:
        print(*ans)
    else:
        print(-1)
