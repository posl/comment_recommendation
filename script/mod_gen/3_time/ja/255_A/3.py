def main():
    R, C = map(int, input().split())
    A = [[int(i) for i in input().split()] for j in range(2)]
    print(A[R-1][C-1])

if __name__ == '__main__':
    main()