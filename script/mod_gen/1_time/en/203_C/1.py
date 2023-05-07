def main():
    N, K = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A, B = zip(*sorted(zip(A, B)))
    A = list(A)
    B = list(B)
    A.append(10 ** 18 + 1)
    B.append(0)
    ans = 0
    for i in range(N):
        if K >= A[i] - ans:
            K -= A[i] - ans
            ans = A[i]
            K += B[i]
        else:
            ans += K
            K = 0
            break
    ans += K
    print(ans)
main()
I have a list of data. I want to find the sum of the list, but only for the numbers that are divisible by 3. I have a list of numbers, and I want to find the sum of only the numbers that are divisible by 3. I have tried to use the sum function, but it doesn’t work. Here is a sample of the list:
[2, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89

if __name__ == '__main__':
    main()