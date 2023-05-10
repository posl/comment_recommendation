def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    result = 'correct'
    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i][j] == 'W':
                    if A[j][i] != 'L':
                        result = 'incorrect'
                elif A[i][j] == 'L':
                    if A[j][i] != 'W':
                        result = 'incorrect'
                elif A[i][j] == 'D':
                    if A[j][i] != 'D':
                        result = 'incorrect'
    print(result)
main()

if __name__ == '__main__':
    main()