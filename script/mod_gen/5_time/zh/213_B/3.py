def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    print(A[1])

if __name__ == '__main__':
    main()