def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    i = 0
    j = N-1
    ans = 0
    while i < j:
        if A[i] == A[j]:
            i += 1
            j -= 1
        elif A[i] < A[j]:
            i += 1
            A[i] += A[i-1]
            ans += 1
        else:
            j -= 1
            A[j] += A[j+1]
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()