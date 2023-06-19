def main():
    # N = int(input())
    # A = list(map(int, input().split()))
    # N = 3
    # A = [1, 7, 1]
    N = 20
    A = [7, 8, 1, 1, 4, 9, 9, 6, 8, 2, 4, 1, 1, 9, 5, 5, 5, 3, 6, 4]
    print(A)
    total = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] != A[j]:
                total += 1
    print(total)

if __name__ == '__main__':
    main()