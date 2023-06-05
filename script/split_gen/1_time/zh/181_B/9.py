def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    max_a = max(a)
    min_b = min(b)
    print(max(0, min_b - max_a + 1))
