def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if N == 2:
        print(A[0] - A[1] + 1)
        return
    if A[0] <= sum(A[1:]):
        print(1)
        return
    print(A[0] - (sum(A[1:]) + 1) // 2 + 1)

if __name__ == '__main__':
    main()