def main():
    n, m = map(int, input().split())
    a = [list(input()) for _ in range(2 * n)]
    rank = [[i, 0] for i in range(2 * n)]
    for i in range(m):
        for j in range(n):
            hand1 = a[rank[2 * j][0]][i]
            hand2 = a[rank[2 * j + 1][0]][i]
            if hand1 == hand2:
                continue
            elif hand1 == 'G':
                if hand2 == 'C':
                    rank[2 * j][1] += 1
                else:
                    rank[2 * j + 1][1] += 1
            elif hand1 == 'C':
                if hand2 == 'P':
                    rank[2 * j][1] += 1
                else:
                    rank[2 * j + 1][1] += 1
            else:
                if hand2 == 'G':
                    rank[2 * j][1] += 1
                else:
                    rank[2 * j + 1][1] += 1
        rank.sort(key=lambda x: (-x[1], x[0]))
    for i in range(2 * n):
        print(rank[i][0] + 1)
