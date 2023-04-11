#问题Takahashi是一个竞争性编程的新手，他想学习M种算法。
#最初，他对M种算法中的每一种的理解水平是0。
#高桥正在逛一家书店，在那里他找到了N本关于算法的书。
#第i本书（1≦i≦N）的售价为C_i日元（日本的货币）。如果他买下这本书并阅读，他对第j种算法的理解水平将在每个j（1≦ j≦ M）上增加A_{i,j}。
#没有其他方法可以提高算法的理解水平。
#高桥的目标是使他对所有M种算法的理解水平达到X或更高。确定这个目标是否可以实现。如果可以实现，请找出实现这一目标所需的最小资金量。
#
#限制条件
#输入的所有数值都是整数。
#1≦ N, M≦ 12
#1≦ X≦ 10^5
#1≦ C_i ≦ 10^5
#0≦ A_{i, j} ≦ 10^5
#
#输入
#输入是由标准输入法提供的，其格式如下：
#N M X
#C_1 A_{1,1} A_{1,2} ...A_{1,M}
#C_2 A_{2,1} A_{2,2} ...A_{2,M}
#.
#.
#.
#C_N A_{N,1} A_{N,2} ...A_{N,M}
#
#输出
#如果目标无法实现，打印-1；否则，打印实现目标所需的最小资金量。
#
#输入样本 1
#3 3 10
#60 2 2 4
#70 8 7 9
#50 2 3 9
#
#样本输出1
#120
#购买第二本和第三本，使他对所有算法的理解水平达到10或更高，并尽可能地减少费用。
#
#样本输入 2
#3 3 10
#100 3 1 4
#100 1 5 9
#100 2 6 5
#
#样本输出2
#-1
#购买所有的书仍然不足以使他对所有算法的理解水平达到10或更高。
#
#样本输入3
#8 5 22
#100 3 7 5 3 1
#164 4 5 2 7 8
#334 7 2 7 2 9
#234 4 7 2 8 2
#541 5 4 3 3 6
#235 4 8 6 9 7
#394 3 6 1 6 2
#872 8 4 3 7 2
#
#样本输出3
#1067

def 