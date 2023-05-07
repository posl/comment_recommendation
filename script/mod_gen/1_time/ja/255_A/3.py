def main():
    r, c = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(2)]
    print(A[r-1][c-1])

if __name__ == '__main__':
    main()