def main():
    N, M = map(int, input().split())
    rooms = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        rooms[a-1].append(b-1)
        rooms[b-1].append(a-1)
    visited = [False] * N
    visited[0] = True
    stack = [0]
    while stack:
        r = stack.pop()
        for i in rooms[r]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
    if not all(visited):
        print('No')
        return
    print('Yes')
    visited = [False] * N
    visited[0] = True
    stack = [0]
    while stack:
        r = stack.pop()
        for i in rooms[r]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
                print(r+1)
                break
