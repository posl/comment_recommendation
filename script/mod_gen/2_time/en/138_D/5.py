def main():
    N, Q = map(int, input().split())
    #N, Q = 6, 2
    #a = [1, 1, 2, 3]
    #b = [2, 3, 4, 6]
    #p = [1, 1]
    #x = [10, 10]
    a = []
    b = []
    for i in range(N-1):
        a_i, b_i = map(int, input().split())
        #a_i, b_i = a[i], b[i]
        a.append(a_i)
        b.append(b_i)
    p = []
    x = []
    for i in range(Q):
        p_i, x_i = map(int, input().split())
        #p_i, x_i = p[i], x[i]
        p.append(p_i)
        x.append(x_i)
    #print(a)
    #print(b)
    #print(p)
    #print(x)
    graph = [[] for i in range(N)]
    for i in range(N-1):
        graph[a[i]-1].append(b[i]-1)
        graph[b[i]-1].append(a[i]-1)
    #print(graph)
    #print('-----')
    from collections import deque
    queue = deque()
    queue.append(0)
    visited = [False for i in range(N)]
    visited[0] = True
    parent = [-1 for i in range(N)]
    while len(queue) > 0:
        q = queue.popleft()
        for i in graph[q]:
            if not visited[i]:
                visited[i] = True
                parent[i] = q
                queue.append(i)
    #print(parent)
    #print('-----')
    count = [0 for i in range(N)]
    for i in range(Q):
        count[p[i]-1] += x[i]
    #print(count)
    #print('-----')
    queue = deque()
    queue.append(0)
    visited = [False for i in range(N)]
    visited[0] = True
    while len(queue) > 0:
        q = queue.popleft()
        for i in graph[q]:
            if not visited[i]:
                visited[i] = True
                count[i] += count[q]
                queue.append(i)
    #print(count)
    #print('

if __name__ == '__main__':
    main()