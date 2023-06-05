def main():
    N = int(input())
    A = list(map(int, input().split()))
    min1 = min2 = float('inf')
    for i in range(N):
        if A[i] < min1:
            min2 = min1
            min1 = A[i]
        elif A[i] < min2:
            min2 = A[i]
    for i in range(N):
        if A[i] == min2:
            print(i + 1)
            break

if __name__ == '__main__':
    main()