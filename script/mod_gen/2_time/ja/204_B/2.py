def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if A[i] > 10:
            cnt += A[i] - 10
    print(cnt)

if __name__ == '__main__':
    main()