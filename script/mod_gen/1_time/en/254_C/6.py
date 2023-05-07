def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [i - 1 for i in A]
    if K % 2 == 0:
        if A[0:K//2] == A[K//2:K]:
            print("Yes")
        else:
            print("No")
    else:
        if A[0:K//2] == A[K//2+1:K]:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()