def main():
    N = int(input())
    A = [input() for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                if A[i][j] != '-':
                    print("incorrect")
                    return
            else:
                if A[i][j] == 'W' and A[j][i] != 'L':
                    print("incorrect")
                    return
                elif A[i][j] == 'L' and A[j][i] != 'W':
                    print("incorrect")
                    return
                elif A[i][j] == 'D' and A[j][i] != 'D':
                    print("incorrect")
                    return
    print("correct")

if __name__ == '__main__':
    main()