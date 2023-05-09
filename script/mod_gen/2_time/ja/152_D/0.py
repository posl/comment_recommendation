def main():
    N = int(input())
    A = [0] * 10
    B = [0] * 10
    for i in range(1, N+1):
        A[i//10] += 1
        B[i%10] += 1
    ans = 0
    for i in range(10):
        for j in range(10):
            if i == j:
                ans += A[i] * B[j]
            else:
                ans += A[i] * B[j]
    print(ans)

if __name__ == '__main__':
    main()