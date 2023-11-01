def main():
    n = int(input())
    a = [list(input()) for i in range(n)]
    for i in range(n):
        a[i][i] = '-'
