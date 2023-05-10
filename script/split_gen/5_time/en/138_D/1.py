def main():
    n,q = map(int, input().split())
    nodes = [[] for _ in range(n)]
    for i in range(n-1):
        a,b = map(int, input().split())
        nodes[a-1].append(b-1)
        nodes[b-1].append(a-1)
    values = [0]*n
    for i in range(q):
        p,x = map(int, input().split())
        values[p-1] += x
    stack = [0]
    visited = [False]*n
    visited[0] = True
    while len(stack) > 0:
        parent = stack.pop()
        for child in nodes[parent]:
            if not visited[child]:
                values[child] += values[parent]
                visited[child] = True
                stack.append(child)
    print(' '.join(map(str, values)))
