def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == "W":
                if A[j][i] != "L":
                    print("incorrect")
                    exit()
            elif A[i][j] == "L":
                if A[j][i] != "W":
                    print("incorrect")
                    exit()
            elif A[i][j] == "D":
                if A[j][i] != "D":
                    print("incorrect")
                    exit()
    print("correct")
