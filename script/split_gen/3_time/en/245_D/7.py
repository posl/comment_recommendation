def main():
    # Input
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    # Solve
    b = [0] * (m + 1)
    for i in range(m + 1):
        b[i] = c[i] - sum([a[j] * b[i - j] for j in range(i)])
    print(' '.join(map(str, b)))
