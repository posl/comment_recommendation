def main():
    #入力
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    #処理
    a.sort()
    b.sort()
    if a[-1] > b[0]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()