def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[N])

if __name__ == '__main__':
    main()