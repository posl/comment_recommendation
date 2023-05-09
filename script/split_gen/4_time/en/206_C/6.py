def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(n):
        cnt += n - (i + 1) - bisect.bisect_right(a, a[i], i + 1)
    print(cnt)
