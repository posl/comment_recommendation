def main():
    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]
    a = [[i*7+j+1 for j in range(7)] for i in range(10**100)]
    for i in range(n):
        for j in range(m):
            a[i][j] = b[i][j]
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                print('No')
                return
    print('Yes')
