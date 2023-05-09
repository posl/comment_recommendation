def main():
    A = input().split()
    A = [int(i) for i in A]
    A.sort()
    print(A[0])

if __name__ == '__main__':
    main()