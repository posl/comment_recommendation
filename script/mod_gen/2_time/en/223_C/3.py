def solve():
    N = int(input())
    A = B = 0
    for i in range(N):
        a, b = map(int, input().split())
        A += a / b
        B += 1 / b
    return A / B
print(solve())

if __name__ == '__main__':
    solve()