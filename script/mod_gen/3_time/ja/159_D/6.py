def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    # A[i]の出現回数を数える
    cnt = [0] * (N+1)
    for a in A:
        cnt[a] += 1
    # A[i]の出現回数の2乗の総和を求める
    sum = 0
    for i in range(N+1):
        sum += cnt[i] * cnt[i]
    # k=1,2,...,N のときの答えを出力
    for k in range(1, N+1):
        print((cnt[A[k]]-1) * (cnt[A[k]]-1) - (sum - cnt[A[k]] * cnt[A[k]]))

if __name__ == '__main__':
    main()