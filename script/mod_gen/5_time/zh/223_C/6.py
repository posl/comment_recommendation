def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    sum = 0
    for i in range(N):
        sum += A[i]/B[i]
    sum /= 2
    sum2 = 0
    for i in range(N):
        sum2 += A[i]
        if sum2 >= sum:
            print(sum2 - (sum2 - A[i]) / B[i])
            break

if __name__ == '__main__':
    main()