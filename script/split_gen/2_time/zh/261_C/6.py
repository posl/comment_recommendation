def main():
    n = int(input())
    A = []
    for i in range(n):
        A.append(list(input()))
    for i in range(n):
        for j in range(n):
            if i != j and A[i][j] == "W":
                if A[j][i] != "L":
                    print("不正确")
                    return
            elif i != j and A[i][j] == "L":
                if A[j][i] != "W":
                    print("不正确")
                    return
            elif i != j and A[i][j] == "D":
                if A[j][i] != "D":
                    print("不正确")
                    return
    print("正确")
