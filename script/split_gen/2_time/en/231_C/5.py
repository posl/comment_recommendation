def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for i in range(q)]
    a.sort()
    for i in range(q):
        print(n - bisect.bisect_left(a, x[i]))
