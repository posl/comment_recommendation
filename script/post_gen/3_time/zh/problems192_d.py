#问题陈述
#给出一个由0到9组成的字符串X和一个整数M。
#设d是X中最大的数字。
#选择一个不小于d+1的整数n并将X看作一个基数，可以得到多少个不大于M的不同整数？
#
#限制条件
#X由0到9组成。
#X的长度在1到60之间（包括60）。
#X不以0开头。
#1 ≦ M ≦ 10^{18}
#
#输入
#输入是由标准输入提供的，格式如下：
#X
#M
#
#输出
#打印答案。
#
#输入样本1
#22
#10
#
#采样输出1
#2
#X中最大的数字是2。
#把X看作是一个基数，我们得到8。
#把X看成一个基数-4的数字，我们得到10。
#这两个值是我们唯一能得到的，并且不大于10。
#
#输入样本 2
#999
#1500
#
#样本输出2
#3
#X中最大的数字是9。
#把X看作是一个基数10的数字，我们得到999。
#把X看成是一个基数11的数字，我们得到1197。
#把X看成是一个基数12的数字，我们得到1413。
#这三个值是我们唯一能得到的，并且不大于1500。
#
#输入样本3
#100000000000000000000000000000000000000000000000000000000000
#1000000000000000000
#
#样本输出3
#1
#通过将X看作是一个基数，我们得到576460752303423488，这是我们唯一可以得到的且不大于100000000000000的值。

def 