def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    for i in range(n):
        print(s - 2 * a[i], end=' ')
