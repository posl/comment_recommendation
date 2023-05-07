def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    #Aの中の最大値を探す
    max_A = 0
    for i in range(N):
        if max_A < A[i]:
            max_A = A[i]
    #Aの中にある数値の個数をカウントする
    cnt_A = [0] * (max_A + 1)
    for i in range(N):
        cnt_A[A[i]] += 1
    #Aの中の数値の個数を累積和にする
    for i in range(max_A):
        cnt_A[i+1] += cnt_A[i]
    #Aの中にある数値の個数を累積和にする
    cnt_A = [0] + cnt_A
    #Aの中にある数値の個数を累積和にする
    cnt_A = [0] + cnt_A
    #Aの中にある数値の個数を累積和にする
    cnt_A = [0] + cnt_A
    #Aの中の数値の個数を累積和にする
    for i in range(max_A):
        cnt_A[i+1] += cnt_A[i]
    #Aの中にある数値の個数を累積和にする
    cnt_A = [0] + cnt_A
    #Aの中にある数値の個数を累積和にする
    cnt_A = [0] + cnt_A
    #Aの中にある数値の個数を累積和にする
    cnt_A = [0] + cnt_A
    #Aの中の数値の個数を累積和にする
    for i in range(max_A):
        cnt_A[i+1] += cnt_A[i]
    #Aの中にある数値の個数を累積和にする
    cnt_A = [0] + cnt_A
    #Aの中にあ

if __name__ == '__main__':
    main()