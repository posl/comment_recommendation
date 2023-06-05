def main():
    N = int(input())
    A = list(map(int, input().split()))
    #A = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000,100000000, 1000000000]
    #A = [7, 8, 1, 1, 4, 9, 9, 6, 8, 2, 4, 1, 1, 9, 5, 5, 5, 3, 6, 4]
    #A = [1, 7, 1]
    A.sort()
    prev = -1
    prev_count = 0
    prev_count_sum = 0
    for i in range(N):
        if prev == A[i]:
            prev_count += 1
        else:
            prev_count_sum += (prev_count * (prev_count - 1)) // 2
            prev = A[i]
            prev_count = 1
    prev_count_sum += (prev_count * (prev_count - 1)) // 2
    print((N * (N - 1)) // 2 - prev_count_sum)

if __name__ == '__main__':
    main()