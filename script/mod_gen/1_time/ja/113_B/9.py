def main():
    #入力
    n = int(input())
    t,a = map(int,input().split())
    h = list(map(int,input().split()))
    #平均気温をリスト化
    temp = [t-h[i]*0.006 for i in range(n)]
    #平均気温と目標気温の差をリスト化
    diff = [abs(temp[i]-a) for i in range(n)]
    #最小値を出力
    print(diff.index(min(diff))+1)

if __name__ == '__main__':
    main()