def main():
    n,m,q = map(int,input().split())
    q_list = []
    for i in range(q):
        q_list.append(list(map(int,input().split())))
    print(q_list)
    a = [0] * n
    def dfs(i):
        if i == n:
            print(a)
            return
        for j in range(m):
            a[i] = j
            dfs(i+1)
    dfs(0)
main()
