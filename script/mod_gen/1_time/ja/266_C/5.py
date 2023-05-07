def main():
    #input
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    #output
    if (A[0]-C[0])*(B[1]-D[1]) == (A[1]-C[1])*(B[0]-D[0]):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()