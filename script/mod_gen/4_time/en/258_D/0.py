def solve():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    min_time = 10 ** 9 * 2 * N
    for i in range(N):
        time = 0
        for j in range(N):
            if j <= i:
                time += A[j] + B[j]
            else:
                time += B[j]
        #print("i = ", i, "time = ", time)
        if min_time > time:
            min_time = time
    print(min_time * X)

if __name__ == '__main__':
    solve()