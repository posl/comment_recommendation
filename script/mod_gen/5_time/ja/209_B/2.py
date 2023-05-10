def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            sum += A[i-1] - 1
        else:
            sum += A[i-1]
    if sum <= X:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()