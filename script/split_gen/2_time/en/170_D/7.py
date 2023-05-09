def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A_i が素数かどうかを格納するリスト
    is_prime = [True] * (10**6 + 1)
    # A_i が素数かどうかを判定する
    for i in range(2, (10**6 + 1)):
        if is_prime[i]:
            for j in range(i * 2, (10**6 + 1), i):
                is_prime[j] = False
    # A_i が素数の場合のみ、A_i で割り切れる数を除外する
    for i in range(N):
        if is_prime[A[i]]:
            for j in range(A[i], (10**6 + 1), A[i]):
                is_prime[j] = False
    # A_i が素数の数をカウントする
    count = 0
    for i in range(N):
        if is_prime[A[i]]:
            count += 1
    print(count)
