def main():
    R,C = map(int, input().split())
    A = []
    for i in range(R):
        A.append(list(map(int, input().split())))
    print(A[R-1][C-1])

if __name__ == '__main__':
    main()