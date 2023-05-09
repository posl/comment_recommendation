def main():
    n = int(input())
    A = [0] * n
    B = [0] * n
    for i in range(n):
        A[i], B[i] = map(int, input().split())
    d = [0] * (10 ** 9 + 1)
    for a, b in zip(A, B):
        d[a - 1] += 1
        d[a + b - 1] -= 1
    for i in range(1, 10 ** 9):
        d[i] += d[i - 1]
    for i in range(1, n + 1):
        print(d.count(i))
