def main():
    N = int(input())
    tree = [[] for i in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    colors = [0] * N
    color = 1
    for i in range(N):
        used = set()
        for j in tree[i]:
            used.add(colors[j])
        for j in tree[i]:
            if colors[j] == 0:
                for k in range(1, N+1):
                    if k not in used:
                        colors[j] = k
                        used.add(k)
                        break
    print(max(colors))
    for i in colors:
        if i != 0:
            print(i)
