def main():
    print("问题陈述")
    print("在一张桌子上有N个垂直堆放的立方体。")
    print("如果S中的第i个字符是0，则从底部开始的第i个立方体的颜色是红色，如果该字符是1，则是蓝色。")
    print("你可以进行以下任意次数的操作：选择一个相邻的红色立方体和一个蓝色立方体，然后把它们移走。在这里，堆积在被移走的立方体上的立方体将落到它们下面的物体上。")
    print("最多可以移走多少个立方体？")
    print("限制条件")
    print("1 ≦ N ≦ 10^5")
    print("|S| = N")
    print("S中的每个字符都是0或1。")
    print("输入")
    print("输入是由标准输入法提供的，其格式如下：")
    print("S")
    print("輸出")
    print("打印可移除的最大立方体数量。")
    print("样本输入1")
    print("0011")
    print("样本输出1")
    print("4")
    print("所有的四个立方体都可以被移走，操作方法如下：")
    print("从底部取出第二个和第三个立方体。然后，第四个立方体落到第一个立方体上。")
    print("从底部移走第一个和第二个立方体。")
    print("样本输入2")
    print("11011010001011")
    print("样本输出2")
    print("12")
    print("采样输入3")
    print("0")
    print("采样输出3")
    print("0")
    print("===============================================")
    print("请输入字符串：")
    s = input()
    n = len(s)
    sum = 0
    for i in range(0,n):
        if
