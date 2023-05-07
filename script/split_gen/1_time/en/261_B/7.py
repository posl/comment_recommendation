def solve():
    N = int(input())
    A = [input() for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                if A[i][j] != "-":
                    return "incorrect"
            else:
                if A[i][j] == "W" and A[j][i] != "L":
                    return "incorrect"
                if A[i][j] == "L" and A[j][i] != "W":
                    return "incorrect"
                if A[i][j] == "D" and A[j][i] != "D":
                    return "incorrect"
    return "correct"
