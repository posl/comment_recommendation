def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max = A[0]
    for i in range(1, N):
        if A[i] > max:
            max = A[i]
    for i in range(K):
        if B[i] == max:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()