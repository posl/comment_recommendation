#问题陈述
#我们有N件行李，称为行李1到N，有M个箱子，称为箱子1到M。
#行李i的大小为W_i，价值为V_i。
#箱子i可以包含一件行李，其大小最多为X_i。它不能包含两件或多件行李。
#你将会得到Q个查询。在每个查询中，给定两个整数L和R，解决以下问题：
#问题：在M个箱子中，R-L+1个箱子，箱子L,L+1,...,R，已经无法使用。
#找出我们可以同时放入剩余箱子的一组行李的最大可能总价值。
#
#限制条件
#1 ≦ N ≦ 50
#1 ≦ M ≦ 50
#1 ≦ Q ≦ 50
#1 ≦ W_i ≦ 10^6
#1 ≦ V_i ≦ 10^6
#1 ≦ X_i ≦ 10^6
#1 ≦ L ≦ R ≦ M
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#N M Q
#W_1 V_1
#.
#.
#.
#W_N V_N
#X_1 ...X_M
#查询_1
#.
#.
#.
#查询_Q
#每个查询的格式如下：
#L R
#
#输出
#打印Q行。
#第i行应该包含Query_i所描述的问题的答案。
#
#输入样本 1
#3 4 3
#1 9
#5 3
#7 8
#1 8 6 9
#4 4
#1 4
#1 3
#
#样本输出1
#20
#0
#9
#在第1个查询中，只有箱子4是不可用的。
#通过将行李1放入盒子1，行李3放入盒子2，行李2放入盒子3，我们可以将所有的行李放入盒子，使得盒子里的行李总价值为20。
#在第2个查询中，所有箱子都不可用；答案是0。
#在第3次查询中，只有盒子4是可用的。通过将行李1放入盒子4，我们可以使盒子里的行李总价值为9，这是可能的最大结果。

def 