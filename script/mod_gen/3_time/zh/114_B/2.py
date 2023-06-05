def main():
    #输入
    S = input()
    #初期化
    min_diff = 999
    #逐个取出三个连续的数字
    for i in range(len(S)-2):
        #取出数字
        X = int(S[i:i+3])
        #计算与753的差值
        diff = abs(X-753)
        #更新最小值
        if diff < min_diff:
            min_diff = diff
    #输出
    print(min_diff)

if __name__ == '__main__':
    main()