def main():
    n,m = map(int,input().split())
    node = [[] for i in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        node[a-1].append(b)
        node[b-1].append(a)
    for i in range(n):
        print(len(node[i]),end=' ')
        for j in node[i]:
            print(j,end=' ')
        print()
