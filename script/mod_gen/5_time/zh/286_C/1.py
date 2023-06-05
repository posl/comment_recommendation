def solve():
    N, A, B = map(int, input().split())
    S = input()
    S = list(S)
    ans = 0
    k = 0
    for i in range(N // 2):
        if S[i] != S[N - 1 - i]:
            k += 1
    if k == 0:
        print(ans)
        return
    if A < B:
        ans += A * k
        print(ans)
        return
    else:
        ans += B * k
    if k == 1:
        print(ans)
        return
    if k == 2:
        ans += A
        print(ans)
        return
    if k == 3:
        ans += A * 2
        print(ans)
        return
    if k == 4:
        ans += A * 2
        print(ans)
        return
    if k == 5:
        ans += A * 3
        print(ans)
        return
    if k == 6:
        ans += A * 3
        print(ans)
        return
    if k == 7:
        ans += A * 4
        print(ans)
        return
    if k == 8:
        ans += A * 4
        print(ans)
        return
    if k == 9:
        ans += A * 4
        print(ans)
        return
    if k == 10:
        ans += A * 5
        print(ans)
        return
    if k == 11:
        ans += A * 5
        print(ans)
        return
    if k == 12:
        ans += A * 6
        print(ans)
        return
    if k == 13:
        ans += A * 6
        print(ans)
        return
    if k == 14:
        ans += A * 6
        print(ans)
        return
    if k == 15:
        ans += A * 7
        print(ans)
        return
    if k == 16:
        ans += A * 7
        print(ans)
        return
    if k == 17:
        ans += A * 7
        print(ans)
        return
    if k == 18:
        ans += A * 7
        print(ans)
        return
    if

if __name__ == '__main__':
    solve()