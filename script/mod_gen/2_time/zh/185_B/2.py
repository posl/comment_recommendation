def main():
    A = [int(i) for i in input().split()]
    A.sort()
    if A[0] + A[1] + A[2] + A[3] < 500:
        print(4)
    elif A[0] + A[1] + A[2] < 500:
        print(3)
    elif A[0] + A[1] < 500:
        print(2)
    else:
        print(1)

if __name__ == '__main__':
    main()