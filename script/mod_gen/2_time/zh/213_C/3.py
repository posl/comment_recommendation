def main():
    N = int(input())
    A = list(map(int, input().split()))
    min1 = min2 = 10**9
    for i in range(N):
        if A[i] < min1:
            min2 = min1
            min1 = A[i]
            min_index = i
        elif A[i] < min2:
            min2 = A[i]
    print(min_index + 1)

if __name__ == '__main__':
    main()