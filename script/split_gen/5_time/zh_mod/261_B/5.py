def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    flag = True
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == "W" and A[j][i] != "L":
                flag = False
                break
            if A[i][j] == "L" and A[j][i] != "W":
                flag = False
                break
            if A[i][j] =
