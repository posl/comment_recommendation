#问题陈述
#给你一个长度为N的非负整数的序列。
#当B是一个从A中选择K个元素并在不改变顺序的情况下将它们连接起来得到的序列时，请找出MEX(B)的最大可能值。
#这里，对于一个序列X，我们将MEX(X)定义为满足以下条件的唯一非负整数m：
#每个整数i，使0≦i<m包含在X中。
#m不包含在X中。
#
#约束条件
#输入的所有数值都是整数。
#1 ≦ k ≦ n ≦ 3 × 10^5
#0 ≦ A_i ≦ 10^9
#
#输入
#输入是由标准输入提供的，格式如下：
#N K
#A_1 A_2 ...A_N
#
#输出
#打印答案。
#
#输入样本 1
#7 3
#2 0 2 3 2 1 9
#
#样本输出 1
#3
#在这个输入中，A=(2,0,2,3,2,1,9)，你通过挑选K=3个元素得到序列B。  比如说、
#如果选择第1、2、3个元素，MEX(B)=MEX(2,0,2)=1。
#如果选择第3、4和6个元素，MEX(B)=MEX(2,3,1)=0。
#如果选择第2、6和7个元素，MEX(B)=MEX(0,1,9)=2。
#如果选择第2、第3和第6个元素，MEX(B)=MEX(0,2,1)=3。
#最大可能的MEX是3。

def 