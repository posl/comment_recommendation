def solve():
    A = list(map(int, input().split()))
    A.sort()
    if A[0] + A[1] + A[2] + A[3] <= 300:
        print(1)
    elif A[0] + A[1] + A[2] <= 300 or A[1] + A[2] + A[3] <= 300:
        print(2)
    else:
        print(3)

if __name__ == '__main__':
    solve()