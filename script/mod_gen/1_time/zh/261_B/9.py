def main():
    n = int(input())
    A = []
    for i in range(n):
        A.append(list(input()))
    for i in range(n):
        for j in range(n):
            if A[i][j] == 'W':
                if A[j][i] != 'L':
                    print("不正确")
                    return
            elif A[i][j] == 'L':
                if A[j][i] != 'W':
                    print("不正确")
                    return
            elif A[i][j] == 'D':
                if A[j][i] != 'D':
                    print("不正确")
                    return
    print("正确")

if __name__ == '__main__':
    main()