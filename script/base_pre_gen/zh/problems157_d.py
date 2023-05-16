#问题陈述
#一个SNS有N个用户--用户1，用户2，...，用户N。
#在这N个用户之间，有一些关系--M条友谊和K条阻隔。
#对于每个i = 1, 2, ..., M，用户A_i和用户B_i之间有一个双向的友谊。
#对于每个i = 1, 2, ..., K，在用户C_i和用户D_i之间有一个双向的封锁关系。
#当以下四个条件都满足时，我们定义用户a为用户b的候选好友：
#a ≠ b。
#用户a和用户b之间不存在友谊。
#用户a和用户b之间不存在blockhip。
#存在一个由1到N（包括）之间的整数组成的序列c_0, c_1, c_2, ..., c_L，使得c_0 = a, c_L = b，并且对于每个i = 0, 1, ..., L - 1的用户c_i和c_{i+1}之间存在友谊。
#对于每个用户i = 1, 2, ...N，它有多少个朋友候选人？
#
#限制条件
#输入的所有数值都是整数。
#2 ≤ N ≤ 10^5
#0 ≦ M ≦ 10^5
#0 ≦ K ≦ 10^5
#1 ≦ A_i, B_i ≦ N
#A_i ≠ B_i
#1 ≦ C_i, D_i ≦ N
#C_i ≠ D_i
#(A_i, B_i) ≠ (A_j, B_j) (i ≠ j)
#(A_i, B_i) ≠ (B_j, A_j)
#(C_i, D_i) ≠ (C_j, D_j) (i ≠ j)
#(C_i, D_i) ≠ (D_j, C_j)
#(A_i, B_i) ≠ (C_j, D_j)
#(A_i, B_i) ≠ (D_j, C_j)
#
#输入
#输入是由标准输入给出的，格式如下：
#N M K
#A_1 B_1
#.
#.
#.
#A_M B_M
#C_1 D_1
#.
#.
#.
#C_K D_K
#
#输出
#按顺序打印答案，中间有空格。
#
#输入样本 1
#4 4 1
#2 1
#1 3
#3 2
#3 4
#4 1
#
#样本输出1
#0 1 0 1
#用户2和3之间有友谊，3和4之间也有友谊。同时，用户2和4之间没有友谊或阻隔关系。因此，用户4是用户2的候选好友。
#然而，用户1或3都不是用户2的候选朋友，所以用户2有一个候选朋友。
#
#样本输入2
#5 10 0
#1 2
#1 3
#1 4
#1 5
#3 2
#2 4
#2 5
#4 3
#5 3
#4 5
#
#样本输出2
#0 0 0 0 0
#每个人都是其他人的朋友，没有朋友候选人。
#
#样本输入3
#10 9 3
#10 1
#6 7
#8 2
#2 5
#8 4
#7 3
#10 9
#6 4
#5 8
#2 6
#7 5
#3 1
#
#输出样本3
#1 3 5 4 3 3 3 3 1 0

def 