def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                if A[i][j] != '-':
                    print("incorrect")
                    exit()
            else:
                if A[i][j] == 'W' and A[j][i] != 'L':
                    print("incorrect")
                    exit()
                elif A[i][j] == 'L' and A[j][i] != 'W':
                    print("incorrect")
                    exit()
                elif A[i][j] == 'D' and A[j][i] != 'D':
                    print("incorrect")
                    exit()
    print("correct")
main()
