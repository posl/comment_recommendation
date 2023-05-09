def main():
    N = int(input())
    #N以下の正整数の中から等確率で 1 つを選んで a とする。
    #このとき、a が奇数である確率を答える。
    #N が奇数のとき、N 以下の奇数は N/2+1 個
    #N が偶数のとき、N 以下の奇数は N/2 個
    if N % 2 == 0:
        print(N/2/N)
    else:
        print((N+1)/2/N)

if __name__ == '__main__':
    main()