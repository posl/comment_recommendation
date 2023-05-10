def solve():
    A, B = map(int, input().split())
    ans = 1
    for i in range(A - B):
        ans *= 32
    print(ans)

if __name__ == '__main__':
    solve()