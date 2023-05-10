def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # AとBの差をとる
    diff = [abs(A[i]-B[i]) for i in range(N)]
    # 1つ目の条件を満たすか判定
    for i in range(N):
        if diff[i] > K:
            print('No')
            return
    # 2つ目の条件を満たすか判定
    tmp = [0] * N
    tmp[0] = 1
    for i in range(N-1):
        if diff[i] <= K:
            tmp[i+1] = 1
        else:
            tmp[i+1] = 0
    if sum(tmp) == N:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()