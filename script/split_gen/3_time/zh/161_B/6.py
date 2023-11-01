def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(n):
        sum += a[i]
    if a[m-1] >= su
