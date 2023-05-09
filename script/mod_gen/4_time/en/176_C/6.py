def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    h = 0
    for i in range(N):
        if A[i] > h + 1:
            print(-1)
            return
        elif A[i] == h + 1:
            h += 1
    print(sum(A))
solve()

if __name__ == '__main__':
    solve()