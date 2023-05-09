def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    left = 0
    right = 0
    for i in range(n):
        left += a[i] / b[i]
    for i in range(n):
        right += a[i] / b[n - i - 1]
    print(left/2 + right/2)
