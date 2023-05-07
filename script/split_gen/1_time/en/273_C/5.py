def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    c = [0] * (n+1)
    for i in range(n):
        c[a[i]] += 1
    s = [0] * (n+1)
    for i in range(1, n+1):
        s[i] = s[i-1] + c[i]
    for i in range(n):
        print(s[a[i]] - 1)
