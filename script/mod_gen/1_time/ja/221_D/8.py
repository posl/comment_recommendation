def main():
    N = int(input())
    # A_i と B_i を格納する配列を用意
    A = []
    B = []
    for i in range(N):
        # A_i, B_i をスペース区切りで受け取る
        A_i, B_i = map(int, input().split())
        # A_i, B_i をそれぞれ配列に格納
        A.append(A_i)
        B.append(B_i)
    # D_i を格納する配列を用意
    D = [0] * N
    # 1 人がログインしている日数を格納する配列を用意
    one = [0] * (10 ** 9 + 1)
    # 2 人がログインしている日数を格納する配列を用意
    two = [0] * (10 ** 9 + 1)
    # 3 人がログインしている日数を格納する配列を用意
    three = [0] * (10 ** 9 + 1)
    # 1 人がログインしている日数を計算
    for i in range(N):
        one[A[i]] += 1
        one[A[i] + B[i]] -= 1
    # 1 人がログインしている日数の累積和を計算
    for i in range(1, 10 ** 9 + 1):
        one[i] += one[i - 1]
    # 2 人がログインしている日数を計算
    for i in range(N):
        if one[A[i]] >= 2:
            two[A[i]] += 1
            two[A[i] + B[i]] -= 1
    # 2 人がログインしている日数の累積和を計算
    for i in range(1, 10 ** 9 + 1):
        two[i] += two[i - 1]
    # 3 人がログインしている日数を計算
    for i in range(N):
        if two[A[i]] >= 1:

if __name__ == '__main__':
    main()