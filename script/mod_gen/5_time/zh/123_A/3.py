def main():
    # 读取输入
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    # 用列表存储天线坐标
    antenna = [a, b, c, d, e]
    # 遍历列表，判断是否有天线间距大于k
    for i in range(0, 4):
        for j in range(i+1, 5):
            if antenna[j] - antenna[i] > k:
                print(':(')
                return
    # 若没有天线间距大于k，则输出Yay!
    print('Yay!')

if __name__ == '__main__':
    main()