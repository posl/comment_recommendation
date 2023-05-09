def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.insert(0, 0)
    A.append(0)
    L = 0
    R = 0
    ans = 0
    for i in range(1, N+1):
        for j in range(i+1, N+2):
            while A[L] * A[j] < A[i] * A[R]:
                L += 1
            while A[L] * A[j] > A[i] * A[R]:
                R += 1
            if A[L] * A[j] == A[i] * A[R]:
                ans += R - L
    print(ans)

if __name__ == '__main__':
    main()