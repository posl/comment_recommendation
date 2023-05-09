def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_max = max(A)
    A_max_idx = A.index(A_max)
    for i in range(N):
        if i == A_max_idx:
            print(max(A[:i]+A[i+1:]))
        else:
            print(A_max)

if __name__ == '__main__':
    main()