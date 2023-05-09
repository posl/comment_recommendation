def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    s = 0
    for i in range(n):
        for j in range(i+1, n):
            s += a[i] + a[j]
            if j-i+1 == m:
                break
    print(s)
