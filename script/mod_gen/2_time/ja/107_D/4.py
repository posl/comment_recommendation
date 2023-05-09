def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 累積和を求める
    cumsum = [0]
    for i in range(N):
        cumsum.append(cumsum[i] + A[i])
    # 累積和の差の絶対値を求める
    diff = [0]
    for i in range(N):
        diff.append(abs(cumsum[i+1] - cumsum[i]))
    # 累積和の差の絶対値の中央値を求める
    diff.sort()
    print(diff[N//2])

if __name__ == '__main__':
    main()