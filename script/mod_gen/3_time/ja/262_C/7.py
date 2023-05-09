def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i, a in enumerate(A):
        if a > i + 1:
            continue
        if A[a - 1] == i + 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()