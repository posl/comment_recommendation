def main():
    R, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(2)]
    print(A[1-R][1-C])

if __name__ == '__main__':
    main()