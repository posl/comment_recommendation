def main():
    A = [int(i) for i in input().split()]
    A.sort()
    print(A[2]-A[0])

if __name__ == '__main__':
    main()