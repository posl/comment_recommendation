def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        edges.append(list(map(int,input().split())))
    edges.sort(key=lambda x:x[2])
    #print(edges)
    ans = 0
    for i in range(N-1):
        ans += edges[i][2]*(i+1)*(N-i-1)
    print(ans)

if __name__ == '__main__':
    main()