def solve():
    N, x, y = map(int, input().split())
    A = [int(n) for n in input().split()]
    for i in range(N):
        for j in range(i+1, N):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    A = [0] + A
    A.append(0)
    for i in range(N+1):
        if A[i] + A[i+1] > A[-1]:
            print("No")
            return
    print("Yes")
    return
solve()

if __name__ == '__main__':
    solve()