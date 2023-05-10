def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N < M:
        print("No")
        exit()
    A.sort(reverse=True)
    B.sort(reverse=True)
    for i in range(M):
        if A[i] < B[i]:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()