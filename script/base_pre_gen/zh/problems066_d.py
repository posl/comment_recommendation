#问题陈述
#给你一个长度为n+1的整数序列，a_1,a_2,...,a_{n+1}，它由n个整数1,...,n组成。
#众所周知，n个整数1,...,n中的每一个都在这个序列中至少出现一次。
#对于每个整数k=1,...,n+1，请找出长度为k的该序列的不同子序列（不一定是连续的）的数量，模数为10^9+7。
#
#注意事项
#如果两个子序列的内容相同，即使它们来自原序列的不同位置，也不会被单独计算。
#长度为k的序列a的子序列是通过选择a中的k个元素并在不改变其相对顺序的情况下排列得到的序列。例如，序列1,3,5和1,2,3是1,2,3,4,5的子序列，而3,1,2和1,10,100则不是。
#
#
#约束条件
#1 ≦ n ≦ 10^5
#1 ≦ a_i ≦ n
#整数1,...,n中的每一个都出现在这个序列中。
#n和a_i是整数。
#
#输入
#输入是由标准输入给出的，格式如下：
#n
#a_1 a_2 ... a_{n+1}。
#
#输出
#打印n+1行。
#第k行应该包含长度为k的给定序列的不同子序列的数量，模数为10^9+7。
#
#输入样本 1
#3
#1 2 1 3
#
#样本输出 1
#3
#5
#4
#1
#有三个长度为1的子序列：1、2和3。
#有五个长度为2的子序列：1,1和1,2和1,3以及2,1和2,3。
#有四个长度为3的子序列：1，1，3和1，2，1和1，2，3和2，1，3。
#有一个长度为4的子序列：1,2,1,3。
#
#输入样本2
#1
#1 1
#
#样本输出2
#1
#1
#有一个长度为1的子序列：1。
#有一个长度为2的子序列：1,1。
#
#输入样本 3
#32
#29 19 7 10 26 32 27 4 11 20 2 8 16 23 5 14 6 12 17 22 18 30 28 24 15 1 25 3 13 21 19 31 9
#
#样本输出3
#32
#525
#5453
#40919
#237336
#1107568
#4272048
#13884156
#38567100
#92561040
#193536720
#354817320
#573166440
#818809200
#37158313
#166803103
#166803103
#37158313
#818809200
#573166440
#354817320
#193536720
#92561040
#38567100
#13884156
#4272048
#1107568
#237336
#40920
#5456
#528
#33
#1
#请务必打印出10^9+7的模数。

def 