def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()
    for i in range(K):
        if A[i] <= A[B[i]-1]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()