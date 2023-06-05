def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[1])

if __name__ == '__main__':
    main()