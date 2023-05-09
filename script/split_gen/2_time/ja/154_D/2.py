def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    # 累積和
    s = [0]
    for i in range(N):
        s.append(s[i] + (p[i]+1)/2)
    # 累積和の差分
    d = []
    for i in range(N-K+1):
        d.append(s[i+K] - s[i])
    print(max(d))
