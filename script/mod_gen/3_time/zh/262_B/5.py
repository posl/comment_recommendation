def main():
    n,m = map(int,input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int,input().split())))
    print(edges)
    count = 0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            for k in range(j+1,n+1):
                if [i,j] in edges and [j,k] in edges and [k,i] in edges:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()