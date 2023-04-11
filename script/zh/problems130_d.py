#问题陈述
#给你一个长度为N的正整数序列，A=a_1,a_2,...,a_{N}，和一个整数K。
#有多少个A的连续子序列满足以下条件？
#(条件）连续的子序列中的元素之和至少是K。
#如果两个连续的子序列来自A中的不同位置，我们认为它们是不同的，即使它们的内容是相同的。
#请注意，答案可能不适合32位整数类型。
#
#约束条件
#1 ≦ a_i ≦ 10^5
#1 ≦ N ≦ 10^5
#1 ≦ K ≦ 10^{10}
#
#输入
#输入是由标准输入法提供的，其格式如下：
#N K
#a_1 a_2 ... a_N
#
#输出
#打印满足条件的A的连续子序列的数量。
#
#输入样本 1
#4 10
#6 1 2 7
#
#样本输出 1
#2
#以下两个连续的子序列满足条件：
#A[1...4]=a_1,a_2,a_3,a_4, 总和为16
#A[2...4]=a_2,a_3,a_4, 总和为10
#
#样本输入 2
#3 5
#3 3 3
#
#样本输出 2
#3
#请注意，如果两个连续的子序列来自不同的位置，我们认为它们是不同的，即使它们的内容相同。
#
#输入样本3
#10 53462
#103 35322 232 342 21099 90000 18843 9010 35221 19352
#
#样本输出3
#36

def 