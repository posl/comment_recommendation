def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    if A[M-1] >= total / (4*M):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()