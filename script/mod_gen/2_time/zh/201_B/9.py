def main():
    A = input().split()
    A.sort()
    if int(A[2])-int(A[1])==int(A[1])-int(A[0]):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()