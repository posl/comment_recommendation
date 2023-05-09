def main():
    n, m, q = map(int, input().split())
    # 1-indexed
    train = [0] * (n + 1)
    for _ in range(m):
        l, r = map(int, input().split())
        train[l] += 1
        train[r + 1] -= 1
    # 累積和
    for i in range(1, n + 1):
        train[i] += train[i - 1]
    # 累積和
    for i in range(1, n + 1):
        train[i] += train[i - 1]
    for _ in range(q):
        p, q = map(int, input().split())
        print(train[q] - train[p - 1])
