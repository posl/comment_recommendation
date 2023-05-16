#问题陈述
#给你一个长度为n的整数序列，a_1，...，a_n。
#让我们考虑对一个空序列b进行以下n次操作。
#第i次操作如下：
#将a_i追加到b的末尾。
#将b中元素的顺序颠倒过来。
#找到经过这n次操作后得到的序列b。
#
#限制条件
#1 ≦ n ≦ 2× 10^5
#0 ≦ a_i ≦ 10^9
#n和a_i是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#n
#a_1 a_2 ... a_n
#
#输出
#在一行中打印n个整数，中间有空格。
#第i个整数应该是b_i。
#
#输入样本 1
#4
#1 2 3 4
#
#样本输出 1
#4 2 1 3
#经过第一步的操作，b变成了：1.
#经过第一步操作的第2步，b变成：1：1.
#在第二步操作的第1步之后，b变成了：1, 2.
#在第二轮操作的第二步之后，b变成了：2，1。
#在第三步操作的第一步之后，b变成了：2，1，3。
#在第三步操作的第二步之后，b变成了：3，1，2：3, 1, 2.
#在第四步操作的第一步之后，b变成：3，1，2：3, 1, 2, 4.
#第四次运算的第二步后，b变成了：4，2，1，3：4, 2, 1, 3.
#因此，答案是4 2 1 3。
#
#输入样本 2
#3
#1 2 3
#
#样本输出 2
#3 1 2
#如上图的样本输出1所示
#，在第三步操作的第二步之后，b变成了3、1、2。因此，答案是3 1 2。
#
#样本输入3
#1
#1000000000
#
#样本输出3
#1000000000
#
#样品输入4
#6
#0 6 7 6 7 0
#
#样本输出 4
#0 6 6 0 7 7

def 