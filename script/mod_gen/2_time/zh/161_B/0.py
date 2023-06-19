def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    S = sum(A)
    for i in range(M):
        if A[i] < S / (4 * M):
            print("否")
            return
    print("是")

if __name__ == '__main__':
    main()