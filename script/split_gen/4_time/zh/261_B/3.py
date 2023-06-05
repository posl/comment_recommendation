def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(input()))
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == 'W':
                if A[j][i] != 'L':
                    print("不正确")
                    return
            if A[i][j] == 'L':
                if A[j][i] != 'W':
                    print("不正确")
                    return
            if A[i][j] == 'D':
                if A[j][i] != 'D':
                    print("不正确")
                    return
    print("正确")
    return
