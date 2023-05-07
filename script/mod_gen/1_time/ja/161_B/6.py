def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) < M * 4:
        print("No")
        return
    A.sort(reverse=True)
    if A[M-1] < sum(A[0:M]) / (4*M):
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()