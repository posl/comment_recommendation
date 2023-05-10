def solve():
    N = int(input())
    A = list(map(int, input().split()))
    s = sum(A)
    for i in range(N):
        print(s-2*A[i], end=" ")
    print()

if __name__ == '__main__':
    solve()