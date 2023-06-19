def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort(reverse=True)
    B.sort(reverse=True)
    i = 0
    j = 0
    cnt = 0
    while i < N and j < N:
        if A[i] > B[j]:
            cnt += 1
            i += 1
        else:
            i += 1
            j += 1
    print(cnt)

if __name__ == '__main__':
    solve()