def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1
    total = 0
    for i in range(N):
        total += d[A[i]] - 1
    for i in range(N):
        print(total - (d[A[i]] - 1))
