def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    print(A[1])
main()

if __name__ == '__main__':
    main()