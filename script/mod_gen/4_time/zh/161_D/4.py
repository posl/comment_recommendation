def main():
    #print("问题陈述\n当且仅当以下条件得到满足时，一个正整数X被认为是一个朗朗上口的数字：\n在X的十进制表示中（不含前导零），对于每一对相邻的数字，这些数字的绝对差值最多为1。\n例如，1234、1和334都是仑数，而31415、119和13579都不是。\n给你一个正整数K，找出第K个最小的伦常数。\n\n限制条件\n1 ≦ K ≦ 10^5\n输入的所有数值都是整数。\n\n输入\n输入由标准输入提供，格式如下：\nK\n\n輸出\n打印答案。\n\n输入样本1\n15\n\n样本输出1\n23\n我们将按升序列出15个最小的朗朗上口数字：\n1,\n2,\n3,\n4,\n5,\n6,\n7,\n8,\n9,\n10,\n11,\n12,\n21,\n22,\n23.\n因此，答案是23。\n\n输入样本2\n1\n\n样本输出2\n1\n\n样品输入3\n13\n\n样品输出3\n21\n\n样本输入4\n100000\n\n样本输出4\n3234566667\n注意，答案可能不适合32位有符号整数类型。")
    k = int(input())
    count = 0
    i = 1
    while True:
        if i < 10:
            count += 1
        else:
            s = str(i)
            flag = True
            for j in range(len(s)-1):
                if abs(int(s[j]) - int(s[j+1])) > 1:
                    flag = False
                    break
            if flag:
                count += 1
        if count == k:
            print(i)
            break
        i += 1
    return 0

if __name__ == '__main__':
    main()