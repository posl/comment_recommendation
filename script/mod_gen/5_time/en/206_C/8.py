def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        count += N - bisect_left(A, A[i]) - 1
    print(count)

if __name__ == '__main__':
    main()