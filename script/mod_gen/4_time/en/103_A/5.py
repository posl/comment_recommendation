def main():
    A = list(map(int, input().split()))
    A.sort()
    print(abs(A[2]-A[0]))

if __name__ == '__main__':
    main()