def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[1] - A[0] + A[2] - A[1])
main()

if __name__ == '__main__':
    main()