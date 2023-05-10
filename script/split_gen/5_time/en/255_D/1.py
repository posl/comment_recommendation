def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    s = sum(a)
    for i in range(q):
        print(n*x[i]+s)
