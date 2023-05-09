def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    # 累積和
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])
    # 累積和の最小値
    minS = [0]
    for i in range(N):
        minS.append(min(minS[i], S[i + 1]))
    # 累積和の最大値
    maxS = [0]
    for i in range(N):
        maxS.append(max(maxS[i], S[i + 1]))
    # P,Q,R,S の最大値と最小値の差の絶対値の最小値を求める
    minDiff = 10 ** 9
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            minDiff = min(minDiff, max(maxS[i] - minS[j], maxS[j] - minS[i]) - (S[i] - S[0]))
    print(minDiff)

if __name__ == '__main__':
    main()