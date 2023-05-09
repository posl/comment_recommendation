def main():
    N, M = map(int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        E[A].append(B)
        E[B].append(A)
    ans = [-1] * N
    ans[0] = 0
    que = [0]
    while que:
        now = que.pop()
        for nxt in E[now]:
            if ans[nxt] == -1:
                ans[nxt] = now
                que.append(nxt)
    if -1 in ans:
        print('No')
    else:
        print('Yes')
        for i in range(1, N):
            print(ans[i] + 1)

if __name__ == '__main__':
    main()