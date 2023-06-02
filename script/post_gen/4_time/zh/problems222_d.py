#问题陈述
#当且仅当s_i ≦ s_{i+1}对每个i(1 ≦ i ≦ n - 1)成立时，n个数的序列S = (s_1, s_2, ..., s_n)，被称为非递减。
#给出的是各为N个整数的非递减序列：A = (a_1, a_2, ..., a_N) 和 B = (b_1, b_2, ..., b_N)。
#考虑一个非递减的N个整数序列，C = (c_1, c_2, ..., c_N)，它满足以下条件：
#a_i ≦ c_i ≦ b_i，对于每一个i（1 ≦ i ≦ N）。
#找出能成为C的序列的数量，模数为998244353。
#
#限制条件
#1 ≦ N ≦ 3000
#0 ≦ a_i ≦ b_i ≦ 3000 (1 ≦ i ≦ N)
#序列A和B是不递减的。
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#N
#a_1 a_2 ... a_N
#b_1 b_2 ... b_N
#
#输出
#打印可以是C的序列的数量，模数为998244353。
#
#输入样本 1
#2
#1 1
#2 3
#
#样本输出 1
#5
#有五个序列可以是C，如下所示。
#(1, 1)
#(1, 2)
#(1, 3)
#(2, 2)
#(2, 3)
#请注意，（2，1）不满足条件，因为它不是非递减的。
#
#样本输入 2
#3
#2 2 2
#2 2 2
#
#样本输出 2
#1
#有一个序列可以是C，如下所示。
#(2, 2, 2)
#
#样本输入3
#10
#1 2 3 4 5 6 7 8 9 10
#1 4 9 16 25 36 49 64 81 100
#
#样本输出3
#978222082
#一定要找到998244353的模数。

def 