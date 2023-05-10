def main():
    n = int(input())
    ab = []
    for _ in range(n-1):
        ab.append(list(map(int, input().split())))
    
    edge = [[] for _ in range(n)]
    for a, b in ab:
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    
    color = [-1] * n
    color[0] = 1
    stack = [0]
    while stack:
        now = stack.pop()
        now_color = color[now]
        for next in edge[now]:
            if color[next] != -1:
                continue
            now_color += 1
            if now_color == color[now]:
                now_color += 1
            color[next] = now_color
            stack.append(next)
    
    print(max(color))
    for i in range(n-1):
        print(color[ab[i][0]-1])
