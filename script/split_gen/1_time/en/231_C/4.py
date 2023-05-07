def main():
    n, q = map(int, input().split())
    a = [int(i) for i in input().split()]
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in x:
        idx = bisect.bisect_left(a, i)
        print(n-idx)
