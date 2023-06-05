def main():
    # 读入数据
    N = int(input())
    a = []
    b = []
    for _ in range(N-1):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # 生成邻接表
    adj = [[] for _ in range(N+1)]
    for i in range(N-1):
        adj[a[i]].append(b[i])
        adj[b[i]].append(a[i])
    # 判断是否是星形
    for i in range(1, N+1):
        if len(adj[i]) == N-1:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()