def solve(N):
    result = 0
    for i in range(1, N+1):
        if i * i > N:
            break
        if N % i == 0:
            if i * i == N:
                result += i
            else:
                result += i + N // i
    return result

if __name__ == '__main__':
    solve()