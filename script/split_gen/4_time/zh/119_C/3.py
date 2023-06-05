def magic(a, b, c, d, e, f, g):
    if a == 0 and b == 0 and c == 0:
        return 0
    if a < 0 or b < 0 or c < 0:
        return 100000000
    return min(magic(a - d, b, c, d, e, f, g) + 1, magic(a, b - e, c, d, e, f, g) + 1, magic(a, b, c - f, d, e, f, g) + 1, magic(a - d, b - e, c, d, e, f, g) + 10, magic(a - d, b, c - f, d, e, f, g) + 10, magic(a, b - e, c - f, d, e, f, g) + 10, magic(a - d, b - e, c - f, d, e, f, g) + 10)
N, A, B, C = map(int, input().split())
l = [int(input()) for i in range(N)]
print(magic(A, B, C, l[0], l[1], l[2], l[3]))
