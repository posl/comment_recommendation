def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    sum = 0
    for i in range(N):
        sum += A[i]
    if sum > X:
        print(N)
    else:
        print((X // sum) * N + N)
main()
