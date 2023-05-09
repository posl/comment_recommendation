def solve():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if A[i] == 1:
            P += 1
        elif A[i] == 2:
            P += 0
        elif A[i] == 3:
            P += 1
        elif A[i] == 4:
            P += 0
    print(P)

if __name__ == '__main__':
    solve()