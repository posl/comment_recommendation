def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max_even = -1
    for i in range(N):
        if A[i] % 2 == 0:
            max_even = A[i]
        else:
            for j in range(i + 1, N):
                if (A[i] + A[j]) % 2 == 0:
                    max_even = max(max_even, A[i] + A[j])
                    break
    print(max_even)

if __name__ == '__main__':
    main()