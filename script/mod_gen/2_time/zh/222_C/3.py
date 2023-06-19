def judge(a, b):
    if a == b:
        return 0
    elif a == "G" and b == "C":
        return 1
    elif a == "G" and b == "P":
        return -1
    elif a == "C" and b == "P":
        return 1
    elif a == "C" and b == "G":
        return -1
    elif a == "P" and b == "G":
        return 1
    elif a == "P" and b == "C":
        return -1
n, m = map(int, input().split())
a = []
for i in range(2*n):
    a.append(input())
rank = [[0]*2 for i in range(n*2)]
for i in range(n*2):
    rank[i][0] = 0
    rank[i][1] = i + 1
for i in range(m):
    for j in range(n):
        p1 = rank[2*j][1] - 1
        p2 = rank[2*j+1][1] - 1
        result = judge(a[p1][i], a[p2][i])
        if result == 1:
            rank[2*j][0] -= 1
        elif result == -1:
            rank[2*j+1][0] -= 1
    rank.sort()
for i in range(n*2):
    print(rank[i][1])

if __name__ == '__main__':
    judge()