def main():
    N = int(input())
    A = [input() for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i][j] == "W" and A[j][i] != "L":
                    print("不正确")
                    return
                elif A[i][j] == "L" and A[j][i] != "W":
                    print("不正确")
                    return
                elif A[i][j] == "D" and A[j][i] != "D":
                    print("不正确")
                    return
    print("正确")
