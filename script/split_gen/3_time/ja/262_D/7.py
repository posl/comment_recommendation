def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    # 1 から N までの整数の和を求める
    sum = 0
    for i in range(1, N+1):
        sum += i
    # 1 から N までの整数の和を N で割った余りを求める
    sum = sum % mod
    # 2^N-1 通りの選び方を求める
    ans = pow(2, N, mod) - 1
    # 2^N-1 通りの選び方を N で割った余りを求める
    ans = ans % mod
    # 2^N-1 通りの選び方を N で割った余りと 1 から N までの整数の和を N で割った余りを掛け合わせる
    ans = ans * sum
    # 2^N-1 通りの選び方を N で割った余りと 1 から N までの整数の和を N で割った余りを掛け合わせたものを N で割った余りを求める
    ans = ans % mod
    print(ans)
