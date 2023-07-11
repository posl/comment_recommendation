def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                pass
            elif A[i][j] == 'W' and A[j][i] != 'L':

if __name__ == '__main__':
    main()