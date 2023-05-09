def main():
    #入力
    N = int(input())
    A = list(map(int,input().split()))
    #最小の非負整数を求める
    for i in range(2001):
        if not i in A:
            print(i)
            break

if __name__ == '__main__':
    main()