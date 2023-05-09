def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    j = 0
    for i in range(N):
        while j < M and B[j] < A[i]:
            j += 1
        if j == M or B[j] != A[i]:
            print('No')
            return
        j += 1
    print('Yes')
solve()

if __name__ == '__main__':
    solve()