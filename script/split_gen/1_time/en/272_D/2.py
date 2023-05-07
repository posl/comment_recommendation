def main():
    n, m = map(int, raw_input().split())
    dist = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = (i - 0) ** 2 + (j - 0) ** 2
    for i in range(n):
        for j in range(n):
            if dist[i][j] == m:
                print 1
            elif dist[i][j] < m:
                print 2
            else:
                print -1
