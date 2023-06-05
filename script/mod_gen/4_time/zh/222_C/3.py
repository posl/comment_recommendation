def rps(a, b):
    if a == b:
        return 0
    elif (a == "G" and b == "C") or (a == "C" and b == "P") or (a == "P" and b == "G"):
        return 1
    else:
        return -1
n, m = map(int, input().split())
a = [list(input()) for _ in range(2*n)]
rank = [[i, 0] for i in range(2*n)]
for i in range(m):
    for j in range(n):
        idx1, idx2 = rank[2*j][0], rank[2*j+1][0]
        res = rps(a[idx1][i], a[idx2][i])
        if res == 1:
            rank[2*j][1] -= 1
        elif res == -1:
            rank[2*j+1][1] -= 1
    rank.sort(key=lambda x: (x[1], x[0]))
for i in range(2*n):
    print(rank[i][0]+1)

if __name__ == '__main__':
    rps()