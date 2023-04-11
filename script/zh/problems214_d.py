#问题陈述
#我们有一棵树，有N个编号为1，2，...，N的顶点。
#第i条边（1 ≦ i ≦ N - 1）连接顶点u_i和顶点v_i，有一个权重w_i。
#对于不同的顶点u和v，让f(u, v)是包含在从顶点u到顶点v的最短路径中的一条边的最大权重。
#求sum_{i = 1}^{N - 1} sum_{j = i + 1}^N f（i, j）。
#
#限制条件
#2 ≦ N ≦ 10^5
#1 ≦ u_i, v_i ≦ N
#1 ≦ w_i ≦ 10^7
#给定的图是一棵树。
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入给出的，格式如下：
#N
#u_1 v_1 w_1
#.
#.
#.
#u_{N - 1} v_{N - 1} w_{N - 1}
#
#输出
#打印答案。
#
#输入样本 1
#3
#1 2 10
#2 3 20
#
#样品输出1
#50
#我们有f（1，2）=10，f（2，3）=20，f（1，3）=20，所以我们应该打印它们的总和，即50。
#
#样本输入2
#5
#1 2 1
#2 3 2
#4 2 5
#3 5 14
#
#样本输出2
#76

def 