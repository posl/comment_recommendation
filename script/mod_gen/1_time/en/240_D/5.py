def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [0] * n
    b[0] = a[0]
    for i in range(1, n):
        b[i] = b[i-1] ^ a[i]
    for i in range(n):
        print(b[i])

if __name__ == '__main__':
    solve()