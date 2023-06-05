def solve():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N//2):
        if S[i] != S[-i-1]:
            ans += 1
    if ans == 0:
        print(0)
    elif ans == 1:
        print(A)
    else:
        print(ans * B + A)

if __name__ == '__main__':
    solve()