def solve():
    n, k, q = map(int, input().split())
    a = [int(i) for i in input().split()]
    l = [int(i) for i in input().split()]
    b = [0] * n
    for i in range(q):
        b[l[i] - 1] += 1
    for i in range(n):
        if a[i] - k + sum(b[:i]) > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    solve()