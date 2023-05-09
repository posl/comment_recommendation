def solve():
    A, B, C, D = map(int, input().split())
    ans = -1
    for i in range(10**5):
        if (A + (B * i)) <= (C * D * i):
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    solve()