def main():
    n, q = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    for _ in range(q):
        i, j = map(int, input().split())
        print(a[i-1][j-1])
