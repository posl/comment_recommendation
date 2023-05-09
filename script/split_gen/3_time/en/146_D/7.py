def main():
    N = int(input())
    #print(N)
    #print("----")
    g = [[] for _ in range(N)]
    for i in range(N-1):
        a,b = map(int,input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    #print(g)
    #print("----")
    c = [0]*(N-1)
    for i in range(N):
        color = 1
        for j in g[i]:
            if j < i:
                continue
            while color in g[i]:
                color += 1
            c[j] = color
            color += 1
    print(max(c))
    for i in range(N-1):
        print(c[i])
