def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i][j] == "W" and A[j][i] != "L":
                    print("incorrect")
                    return
                elif A[i][j] == "L" and A[j][i] != "W":
                    print("incorrect")
