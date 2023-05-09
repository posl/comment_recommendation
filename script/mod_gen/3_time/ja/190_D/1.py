def solve():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if i * (i + 1) // 2 >= N:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    solve()