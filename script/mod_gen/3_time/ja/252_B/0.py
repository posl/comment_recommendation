def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(K):
        A[B[i]-1] = 0
    if max(A) == 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()