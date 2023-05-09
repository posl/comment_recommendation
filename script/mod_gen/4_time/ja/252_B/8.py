def resolve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(K):
        if A[0] < A[B[i]-1]:
            print("Yes")
            exit()
    print("No")

if __name__ == '__main__':
    resolve()