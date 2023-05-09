def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    A_sum = sum(A)
    B_sum = sum(B)
    if A_sum < B_sum:
        print(0)
        return
    else:
        ans = 0
        diff = A_sum - B_sum
        for i in range(N - 1, -1, -1):
            ans += 1
            diff += A[i] + B[i]
            if diff >= 0:
                print(ans)
                return

if __name__ == '__main__':
    main()