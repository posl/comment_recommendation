def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    #Aの要素をカウント
    count = [0] * 200001
    for i in range(N):
        count[A[i]] += 1
    #print(count)
    #countの要素が奇数のものの数を数える
    odd = 0
    for i in range(200001):
        if count[i] % 2 == 1:
            odd += 1
    #print(odd)
    #Nが偶数のとき、oddは必ず0
    #Nが奇数のとき、oddは必ず1
    if N % 2 == 0:
        if odd == 0:
            print(0)
        else:
            print(odd - 1)
    else:
        if odd == 1:
            print(0)
        else:
            print(odd - 1)

if __name__ == '__main__':
    main()