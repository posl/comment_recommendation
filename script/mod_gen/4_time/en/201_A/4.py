def main():
    A = input().split()
    A = [int(i) for i in A]
    A.sort()
    if A[1] - A[0] == A[2] - A[1]:
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()