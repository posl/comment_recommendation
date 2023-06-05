def main():
    N, Q = map(int, input().split())
    S = input()
    # 1-indexedにする
    S = " " + S
    # 累積和
    cum = [0] * (N + 1)
    for i in range(1, N + 1):
        cum[i] = cum[i - 1] + ord(S[i]) - ord("a") + 1
    #print(cum)
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            cum[x] = cum[x] - ord(S[x]) + ord(S[x - 1])
            cum[x - 1] = cum[x - 1] - ord(S[x - 1]) + ord(S[x])
            S = S[:x - 1] + S[x] + S[x - 1] + S[x + 1:]
        else:
            print(cum[x] - cum[x - 1])
