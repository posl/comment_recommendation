def main():
    W = int(input())
    N = W // 2
    A = [2] * N
    A[0] = 1
    print(N)
    print(*A)

if __name__ == '__main__':
    main()