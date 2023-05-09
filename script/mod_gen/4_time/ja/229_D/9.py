def main():
    s = input()
    k = int(input())
    #Xを最大で何個連続させられるか
    #Xの数を数える
    x_count = 0
    for i in range(len(s)):
        if s[i] == 'X':
            x_count += 1
    #Xをk回連続させる
    #Xの数がkより少ない場合はXの数を出力
    if x_count < k:
        print(x_count)
        return
    #Xの数がk以上の場合はkを出力
    print(k)

if __name__ == '__main__':
    main()