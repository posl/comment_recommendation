def main():
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    a = [j for i in a for j in i]
    a.sort()
    print(a[k*k//2])
