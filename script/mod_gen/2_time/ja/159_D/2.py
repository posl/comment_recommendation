def main():
    N = int(input())
    A = list(map(int, input().split()))
    #各数字の出現回数を数える
    count = [0] * N
    for i in range(N):
        count[A[i]-1] += 1
    #出現回数が2以上の数字の組み合わせの数を数える
    sum = 0
    for i in range(N):
        if count[i] >= 2:
            sum += count[i] * (count[i] - 1) // 2
    #k=1,2,...,N に対して以下の問題を解いて、答えをそれぞれ出力する
    for i in range(N):
        if count[A[i]-1] >= 2:
            print(sum - (count[A[i]-1] * (count[A[i]-1] - 1) // 2) + (count[A[i]-1] - 1) * (count[A[i]-1] - 2) // 2)
        else:
            print(0)

if __name__ == '__main__':
    main()