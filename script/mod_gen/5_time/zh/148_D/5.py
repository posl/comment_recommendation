def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == i + 1:
            ans += 1
    if ans == N:
        print(0)
    elif ans == N - 1:
        print(1)
    else:
        if A[0] == 1 or A[N - 1] == N:
            print(1)
        elif A[0] == N or A[N - 1] == 1:
            print(2)
        else:
            print(3)

if __name__ == '__main__':
    solve()