def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    for i in range(N):
        for j in range(N):
            if i == j:
                if A[i][j] == "-":
                    continue
                else:
                    print("incorrect")
                    return
            else:
                if A[i][j] == "W":
                    if A[j][i] == "L":
                        continue
                    else:
                        print("incorrect")
                        return
                elif A[i][j] == "L":
                    if A[j][i] == "W":
                        continue
                    else:
                        print("incorrect")
                        return
                elif A[i][j] == "D":
                    if A[j][i] == "D":
                        continue
                    else:
                        print("incorrect")
                        return
    print("correct")
