def solve():
    A = list(map(int, input().split()))
    print(min(A[0], A[2], A[3], A[1]//2))

if __name__ == '__main__':
    solve()