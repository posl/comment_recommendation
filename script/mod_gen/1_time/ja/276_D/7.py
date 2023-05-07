def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 2で割れる回数と3で割れる回数をそれぞれカウント
    count2 = 0
    count3 = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] /= 2
            count2 += 1
        while A[i] % 3 == 0:
            A[i] /= 3
            count3 += 1
    # 2で割れる回数と3で割れる回数が全て同じであれば、2で割れる回数を出力
    if count2 == count3:
        print(count2)
    else:
        print(-1)

if __name__ == '__main__':
    main()