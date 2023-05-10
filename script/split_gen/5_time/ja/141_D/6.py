def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    for i in range(m):
        a[i] = a[i]//2
    a.sort()
    a.reverse()
    print(sum(a))
