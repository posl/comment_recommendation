def main():
    # 读入字符串
    S = input()
    # 奇数位置（第1个、第3个、第5个......）上的每个字符都是R、U或D。
    # 偶数位置（第2，4，6，...）的每个字符是L，U或D。
    # 从第一个位置开始，判断奇数位置是否为RUD，偶数位置是否为LUD
    result = "Yes"
    for index in range(len(S)):
        if index % 2 == 0:
            if S[index] == "L":
                result = "No"
                break
        else:
            if S[index] == "R":
                result = "No"
                break
    print(result)
    return

if __name__ == '__main__':
    main()