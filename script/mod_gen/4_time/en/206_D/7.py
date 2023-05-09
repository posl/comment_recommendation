def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A2 = A[::-1]
    if A == A2:
        print(0)
        return
    count = 0
    for i in range(N//2):
        if A[i] != A2[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    solve()