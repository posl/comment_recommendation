def main():
    A = list(map(int, input().split()))
    print(min(abs(A[0] - A[1]) + abs(A[1] - A[2]), abs(A[0] - A[2]) + abs(A[1] - A[2]), abs(A[0] - A[1]) + abs(A[0] - A[2])))

if __name__ == '__main__':
    main()