def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if K == 1:
        if A[0] == A[-1]:
            print("Yes")
        else:
            print("No")
    else:
        if A[0] == A[-1]:
            print("Yes")
        else:
            if A[0] == A[K-1] or A[K-1] == A[-1]:
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    main()