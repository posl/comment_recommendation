def main():
    n = int(input())
    tree = [[] for i in range(n)]
    for i in range(n-1):
        a,b = map(int,input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    ans = []
    stack = [0]
    visited = [False] * n
    visited[0] = True
    while stack:
        v = stack.pop()
        ans.append(v+1)
        for u in tree[v]:
            if not visited[u]:
                stack.append(u)
                visited[u] = True
                break
        else:
            if v == 0:
                break
            else:
                stack.append(u)
    print(*ans)
