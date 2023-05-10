def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    s = sum(a[:k])
    if s % d == 0:
        print(s)
    else:
        print(-1)
