def main():
    #input
    A = [int(i) for i in input().split()]
    #process
    A.sort()
    if A[2]-A[1] == A[1]-A[0]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()