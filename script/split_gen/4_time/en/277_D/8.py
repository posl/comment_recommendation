def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(m)
    a.append(m)
    s = 0
    for i in range(n):
        s += a[i+1] - a[i] - 1
    print(s)
