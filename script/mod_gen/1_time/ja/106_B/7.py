def main():
    N = int(input())
    #N = 105
    #N = 7
    #N = 200
    #N = 100
    #N = 50
    #N = 25
    #N = 10
    #N = 5
    #N = 2
    #N = 1
    #N = 0
    # 奇数のリストを作成
    list = [i for i in range(1, N+1) if i % 2 != 0]
    # 約数を求める
    # 約数の個数が8個のリストを作成
    list2 = [i for i in list if len([j for j in range(1, i+1) if i % j == 0]) == 8]
    print(len(list2))

if __name__ == '__main__':
    main()