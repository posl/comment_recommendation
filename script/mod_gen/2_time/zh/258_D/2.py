def solve(N, X, AB):
    A = []
    B = []
    for i in range(N):
        A.append(AB[i][0])
        B.append(AB[i][1])
    #print(N, X, A, B)
    min_time = 10 ** 18
    for i in range(N):
        time = A[i]
        count = 1
        j = i - 1
        while j >= 0:
            time += B[j]
            count += 1
            j -= 1
        time += B[i] * ((X - count) // N)
        count += N * ((X - count) // N)
        j = 0
        while count < X:
            time += B[j]
            count += 1
            j += 1
        min_time = min(min_time, time)
    return min_time

if __name__ == '__main__':
    solve()