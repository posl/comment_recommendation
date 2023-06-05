def main():
    # 读入
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 累積和を計算
    a_acc = [0]
    b_acc = [0]
    for i in range(n):
        a_acc.append(a_acc[i] + a[i])
    for i in range(m):
        b_acc.append(b_acc[i] + b[i])
    # 答えを求める
    ans = 0
    j = m
    for i in range(n + 1):
        if a_acc[i] > k:
            break
        while a_acc[i] + b_acc[j] > k:
            j -= 1
        ans = max(ans, i + j)
    print(ans)
