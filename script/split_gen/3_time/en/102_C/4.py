def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [a[i] - (i + 1) for i in range(n)]
    a.sort()
    med = a[n // 2]
    ans = sum([abs(med - a[i]) for i in range(n)])
    print(ans)
