#问题陈述
#高桥和青木各有一个玩具，用M条绳索系在N个球上。
#在高桥的玩具中，球的编号为1，...，N，第i根绳子系着球A_i和B_i。
#同样地，在Aoki的玩具中，球的编号为1，...，N，第i条绳子系着球C_i和D_i。
#在每个玩具中，没有一条绳子把球绑在自己身上，也没有两个球被两条或更多不同的绳子绑住。
#Snuke想知道这两个玩具是否有相同的形状。
#在这里，当有一个序列P满足以下条件时，就可以说它们有相同的形状。
#P是(1,...,N)的一个置换。
#对于1到N（包括）之间的每一对整数i，j，下面的条件成立。
#当且仅当青木玩具中的球P_i和P_j被绳子绑住时，高桥玩具中的球i和j被绳子绑住。
#
#如果这两个玩具的形状相同，则打印Yes；否则，打印No。
#
#限制条件
#1 ≦ N ≦ 8
#0 ≦ M ≦ ((n(n - 1))/(2))
#1 ≦ A_i < B_i ≦ N (1 ≦ i ≦ M)
#(A_i, B_i) ≠ (A_j, B_j) (i ≠ j)
#1 ≦ C_i < D_i ≦ N (1 ≦ i ≦ M)
#(C_i, D_i) ≠ (C_j, D_j) (i ≠ j)
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入给出的，格式如下：
#N M
#A_1 B_1
#.
#.
#.
#A_M B_M
#C_1 D_1
#.
#.
#.
#C_M D_M
#
#输出
#如果两个玩具的形状相同，则打印Yes；否则，打印No。
#
#输入样本 1
#4 4
#1 2
#1 3
#1 4
#3 4
#1 3
#1 4
#2 3
#3 4
#
#样本输出1
#Yes
#下图左边是高桥的玩具，右边是青木的玩具。
#下图显示这两个玩具有相同的形状。例如，当P=（3，2，1，4）时，声明中的条件得到满足。
#
#输入样本 2
#5 6
#1 2
#1 3
#1 4
#3 4
#3 5
#4 5
#1 2
#1 3
#1 4
#1 5
#3 5
#4 5
#
#样本输出2
#No
#这两个玩具的形状不一样。
#
#样本输入3
#8 0
#
#样本输出3
#Yes

def 