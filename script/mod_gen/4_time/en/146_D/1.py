def main():
    N = int(input())
    G = [[] for i in range(N)]
    for i in range(N-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    #print(G)
    colors = [-1 for i in range(N)]
    colors[0] = 0
    stack = [0]
    while len(stack) > 0:
        v = stack.pop()
        c = 0
        for w in G[v]:
            if colors[w] == -1:
                while c == colors[v]:
                    c += 1
                colors[w] = c
                c += 1
                stack.append(w)
    print(max(colors)+1)
    for i in range(N-1):
        print(colors[i]+1)

if __name__ == '__main__':
    main()