def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    # 1. Aの各要素の出現回数をカウント
    cnt = [0] * N
    for i in range(N):
        cnt[A[i]-1] += 1
    
    # 2. Aの各要素の出現回数を累積和
    for i in range(1,N):
        cnt[i] += cnt[i-1]
    
    # 3. Aの各要素の出現回数を使って、Aの各要素の出現回数の組み合わせを計算
    for i in range(N):
        res = (cnt[N-1] - cnt[A[i]-1]) * (cnt[A[i]-1] - 1) // 2
        print(res)
