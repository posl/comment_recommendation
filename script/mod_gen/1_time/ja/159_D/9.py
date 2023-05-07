def main():
    N = int(input())
    A = list(map(int, input().split()))
    #Aの中に数字が何個あるかを記録する
    #Aの中に数字が何個あるかを記録する
    count = [0] * (N+1)
    for i in range(N):
        count[A[i]] += 1
    #countの中から2個選ぶ組み合わせの数を求める
    count2 = [0] * (N+1) #countの中から2個選ぶ組み合わせの数
    for i in range(N+1):
        count2[i] = count[i] * (count[i] - 1) // 2
    #countの中から2個選ぶ組み合わせの数の合計
    count2sum = 0
    for i in range(N+1):
        count2sum += count2[i]
    #答えを求める
    for i in range(N):
        print(count2sum - count2[A[i]] + (count[A[i]] - 1) * (count[A[i]] - 2) // 2)

if __name__ == '__main__':
    main()