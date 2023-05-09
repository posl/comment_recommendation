def solve():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    ans = ["No"] * N
    for i in range(M):
        ans[S.index(T[i])] = "Yes"
    print("\n".join(ans))

if __name__ == '__main__':
    solve()