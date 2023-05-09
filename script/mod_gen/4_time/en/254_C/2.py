def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K == 1:
        if A == sorted(A):
            print("Yes")
        else:
            print("No")
        exit()
    A1 = A[0::K]
    A2 = A[1::K]
    if sorted(A1) == A1 and sorted(A2) == A2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()