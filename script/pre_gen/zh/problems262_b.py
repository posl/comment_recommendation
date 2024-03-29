#问题陈述
#给你一个有N个顶点和M条边的简单无向图。  顶点编号为1，...，N，第i条（1≦i≦M）边连接着顶点U_i和顶点V_i。
#找出满足以下所有条件的整数组a, b, c的数目：
#1 ≦ a < b < c ≦ N
#有一条边连接顶点a和顶点b。
#有一条边连接着顶点b和顶点c。
#有一条边连接着顶点c和顶点a。
#
#限制条件
#3 ≦ N ≦ 100
#1 ≦ m ≦ ((n(n - 1))/(2))
#1 ≦ U_i < V_i ≦ N (1 ≦ i ≦ M)
#(U_i, V_i) ≠ (U_j, V_j) (i ≠ j)
#输入的所有值都是整数。
#
#输入
#输入是由标准输入给出的，格式如下：
#N M
#U_1 V_1
#.
#.
#.
#U_M V_M
#
#输出
#打印答案。
#
#输入样本 1
#5 6
#1 5
#4 5
#2 3
#1 4
#3 5
#2 5
#
#样本输出 1
#2
#(a, b, c）=（1, 4, 5），（2, 3, 5）满足条件。
#
#样本输入 2
#3 1
#1 2
#
#样本输出2
#0
#
#采样输入3
#7 10
#1 7
#5 7
#2 5
#3 6
#4 7
#1 5
#2 4
#1 3
#1 6
#2 7
#
#样本输出 3
#4

def 