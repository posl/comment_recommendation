#问题说明
#给定一个N个正整数的序列A=(A_1,A_2,...,A_N),找出满足以下条件的1到M(包括)之间的每一个整数k：
#gcd(A_i,k)=1，对每一个整数i来说，1 ≦ i ≦ N。
#
#限制条件
#输入的所有数值都是整数。
#1 ≦ N,M ≦ 10^5
#1 ≦ A_i ≦ 10^5
#
#输入
#输入是由标准输入提供的，格式如下：
#N M
#A_1 A_2 ...A_N
#
#输出
#在第一行，打印x：满足要求的整数的数量。
#在接下来的x行中，打印满足要求的整数，按升序排列，每行都有一个。
#
#输入示例 1
#3 12
#6 1 5
#
#样本输出1
#3
#1
#7
#11
#例如，7具有gcd(6,7)=1,gcd(1,7)=1,gcd(5,7)=1的属性，所以它被包含在满足要求的整数集合中。
#另一方面，9的属性是gcd(6,9)=3，所以它不包括在这个集合中。
#我们有三个介于1和12之间的整数满足这个条件：1，7，和11。请务必按升序打印。

def 