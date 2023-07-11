def main():
    n = int(input())
    A = []
    for i in range(n):
        A.append(input())
    #print(A)
    for i in range(n):
        for j in range(n):
            if i == j:
                pass
            elif A[i][j] == 'W' and A[j][i] != 'L':
                print('incorrect')
                return
            elif A[i][j] == 'L' and A[j][i] != 'W':
                print('incorrect')

if __name__ == '__main__':
    main()