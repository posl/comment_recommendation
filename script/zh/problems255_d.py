#问题陈述
#给你一个长度为N的序列：A=（A_1,A_2,...,A_N）。以下对这个序列的操作被称为操作。
#首先，选择一个整数i，使得1 ≦ i ≦ N。
#接下来，选择并执行以下操作之一。
#给A_i加1。
#从A_i中减去1。
#
#回答Q问题。
#第i个问题是以下内容。
#考虑进行零次或多次操作，将A的每个元素都改为X_i。请找出这样做所需的最少操作数。
#
#限制条件
#输入的所有数值都是整数。
#1 ≦ n,q ≦ 2 × 10^5
#0 ≦ A_i ≦ 10^9
#0 ≦ X_i ≦ 10^9
#
#输入
#输入由标准输入提供，格式如下：
#N Q
#A_1 A_2 ...A_N
#X_1
#X_2
#.
#.
#.
#X_Q
#
#输出
#打印Q行。
#第i行应包含第i个问题的答案，是一个整数。
#
#输入样本 1
#5 3
#6 11 2 5 5
#5
#20
#0
#
#样本输出1
#10
#71
#29
#我们有A=(6,11,2,5,5)，在这个输入中有三个问题。
#对于第1个问题，你可以通过10次操作将A的每个元素变为5，具体操作如下。
#从A_1中减去1。
#从A_2中减去1六次。
#从A_3中加1三次。
#不可能用9次或更少的操作将A的每个元素都变成5。
#对于第2个问题，你可以通过71次操作将A的每个元素变成20。
#对于第3个问题，你可以通过29次运算将A的每个元素变为0。
#
#输入样本 2
#10 5
#1000000000 314159265 271828182 141421356 161803398 0 777777777 255255255 536870912 998244353
#555555555
#321654987
#1000000000
#789456123
#0
#
#样本输出2
#3316905982
#2811735560
#5542639502
#4275864946
#4457360498
#输出可能不适合32位整数。

def 