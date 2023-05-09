def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * n
    for i in range(4 * n - 1):
        c[a[i] - 1] += 1
    for i in range(n):
        if c[i] % 2 == 1:
            print(i + 1)
            break
