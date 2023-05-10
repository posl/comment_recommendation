def solve():
    N = int(input())
    A = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == "W" and A[j][i] != "L":
                return "incorrect"
            elif A[i][j] == "L" and A[j][i] != "W":
                return "incorrect"
            elif A[i][j] == "D" and A[j][i] != "D":
                return "incorrect"
    return "correct"
print(solve())

if __name__ == '__main__':
    solve()