def main():
    N = int(input())
    s = input()
    #白を右端に移動させる
    s = s.replace("R", "0").replace("W", "R").replace("0", "W")
    #白を右端に移動させた後の文字列から、左から順に赤を探し、その位置をリストに格納
    red = [i for i in range(N) if s[i] == "R"]
    #赤の位置のリストから、順に右に移動させるための操作回数を計算
    ans = sum(red[i] - i for i in range(len(red)))
    print(ans)

if __name__ == '__main__':
    main()