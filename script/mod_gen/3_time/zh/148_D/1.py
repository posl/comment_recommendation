def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [0 for i in range(N)]
    for i in range(N):
        if A[i] > N:
            print(-1)
            return
        else:
            B[A[i]-1] = 1
    cnt = 0
    for i in range(N):
        if B[i] == 0:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()