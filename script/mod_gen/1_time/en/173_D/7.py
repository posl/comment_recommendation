def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[:-1]))

if __name__ == '__main__':
    main()