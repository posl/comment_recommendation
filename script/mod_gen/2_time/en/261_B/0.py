def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == 'W':
                if A[j][i] != 'L':
                    print('incorrect')
                    return
            elif A[i][j] == 'L':
                if A[j][i] != 'W':
                    print('incorrect')
                    return
            else:
                if A[j][i] != 'D':
                    print('incorrect')
                    return
    print('correct')

if __name__ == '__main__':
    main()