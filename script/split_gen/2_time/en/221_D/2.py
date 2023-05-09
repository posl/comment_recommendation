def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # 1日目から10^9日目までのログイン数をカウントする
    # ログイン数は最大でもN人なので、10^9日目までのログイン数はN+1人までカウントできる
    count = [0] * (N + 1)
    for i in range(N):
        # ログイン期間の最初の日にログイン数を+1する
        count[A[i]] += 1
        # ログイン期間の最後の日の次の日にログイン数を-1する
        count[A[i] + B[i]] -= 1
    # 1日目から10^9日目までのログイン数を累積和で求める
    for i in range(1, N + 1):
        count[i] += count[i - 1]
    # 1日目から10^9日目までのログイン数の個数をカウントする
    # ログイン数は最大でもN人なので、10^9日目までのログイン数はN+1人までカウントできる
    result = [0] * (N + 1)
    for i in range(N + 1):
        result[count[i]] += 1
    # 1日目から10^9日目までのログイン数の個数を累積和で求める
    for i in range(1, N + 1):
        result[i] += result[i - 1]
    # 1日目から10^9日目までのログイン数の個数を出力する
    for i in range(1, N + 1):
        print(result[i], end=' ')
