def main():
    N = int(input())
    A = list(map(int, input().split()))
    minus = 0
    min_abs = 10**9
    sum = 0
    for i in range(N):
        if A[i] < 0:
            minus += 1
        sum += abs(A[i])
        min_abs = min(min_abs, abs(A[i]))
    if minus % 2 == 0:
        print(sum)
    else:
        print(sum - min_abs * 2)

if __name__ == '__main__':
    main()