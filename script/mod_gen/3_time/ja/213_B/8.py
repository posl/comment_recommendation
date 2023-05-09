def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[1])
main()

if __name__ == '__main__':
    main()