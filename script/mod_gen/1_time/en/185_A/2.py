def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[2] + A[3])

if __name__ == '__main__':
    main()