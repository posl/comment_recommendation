def main():
    # input
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    # compute
    s = sum(a)
    for i in range(q):
        print(s + x[i] * n)
