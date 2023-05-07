def main():
    n, m = [int(x) for x in input().split()]
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = [int(x) for x in input().split()]
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    visited = [False] * n
    def dfs(v):
        visited[v] = True
        for u in adj[v]:
            if not visited[u]:
                dfs(u)
    dfs(0)
    print('Yes' if all(visited) else 'No')
main()
I have a list of lists of strings, and I want to convert it to a list of strings, where each string is the concatenation of the strings in the list of lists. I can do this with a list comprehension, but I think it would be more efficient to do this with a generator expression, but I can't figure out how to do it. My current code is:
