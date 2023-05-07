def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(1, N):
        if A[i] == i+1:
            cnt += 1
            A[i], A[i-1] = A[i-1], A[i]
        elif A[i-1] == i+1:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()