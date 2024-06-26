def main():
    n,m = map(int,input().split())
    a = [input() for _ in range(2*n)]
    rank = [[i,0] for i in range(2*n)]
    for i in range(m):
        for j in range(n):
            p1,p2 = rank[2*j][0],rank[2*j+1][0]
            if a[p1][i] == a[p2][i]:
                continue
            elif a[p1][i] == "G" and a[p2][i] == "C":
                rank[2*j][1] -= 1
            elif a[p1][i] == "C" and a[p2][i] == "P":
                rank[2*j][1] -= 1
            elif a[p1][i] == "P" and a[p2][i] == "G":
                rank[2*j][1] -= 1
            else:
                rank[2*j][1] += 1
    rank.sort(key=lambda x: (x[1],x[0]))
    for i in range(2*n):
        print(rank[i][0]+1)

if __name__ == '__main__':
    main()