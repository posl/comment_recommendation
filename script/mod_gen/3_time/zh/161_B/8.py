def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    sum = 0
    for i in range(M):
        sum += A[i]
    if sum >= sum(A) / (4 * M):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()