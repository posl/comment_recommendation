def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    a_count = 1
    b_count = 1
    for i in range(1, m):
        if a[i] == a[i - 1]:
            a_count += 1
        else:
            a_count = 1
    for i in range(1, m):
        if b[i] == b[i - 1]:
            b_count += 1
        else:
            b_count = 1
    print(a_count * b_count)
