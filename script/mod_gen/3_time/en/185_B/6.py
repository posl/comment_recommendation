def solve():
    # Implement solution here
    N, M, T = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    charge = N
    for i in range(M):
        if i == 0:
            charge -= A[i]
        else:
            charge -= A[i] - B[i - 1]
        if charge <= 0:
            return "No"
        charge += B[i] - A[i]
        if charge > N:
            charge = N
    charge -= T - B[M - 1]
    if charge <= 0:
        return "No"
    return "Yes"
result = solve()
print(result)

if __name__ == '__main__':
    solve()