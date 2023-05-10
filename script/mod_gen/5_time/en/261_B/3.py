def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == 'W' and A[j][i] != 'L':
                print('incorrect')
                return
            elif A[i][j] == 'L' and A[j][i] != 'W':
                print('incorrect')
                return
            elif A[i][j] == 'D' and A[j][i] != 'D':
                print('incorrect')
                return
    print('correct')
    return

if __name__ == '__main__':
    main()