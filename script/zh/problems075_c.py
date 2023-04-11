#问题陈述
#给你一个有N个顶点和M条边的无向连接图，该图不包含自循环和双重边。
#第i条边（1 ≦ i ≦ M）连接顶点a_i和顶点b_i。  
#移除的边使图形断开连接的边被称为桥。
#找出M条边中属于桥的边的数量。  
#
#注释
#自环是一条边i，使得a_i=b_i（1 ≦ i ≦ M）。
#双重边是一对边i,j，使得a_i=a_j和b_i=b_j（1 ≦ i<j ≦ M）。
#当每对顶点之间存在一条路径时，就可以说一个无向图是连通的。
#
#限制条件
#2 ≦ N ≦ 50
#N-1 ≦ M ≦ min(N(N-1)⁄2,50)
#1 ≦ a_i<b_i ≦ N
#给定的图不包含自循环和双边。
#给定的图是连接的。
#
#输入
#输入来自标准输入，其格式如下：  
#N M
#a_1 b_1
#a_2 b_2
#:
#a_M b_M
#
#输出
#打印M条边中属于桥接的边的数量。
#
#输入样本 1
#7 7
#1 3
#2 7
#3 4
#4 5
#4 6
#5 6
#6 7
#
#样本输出1
#4
#下图显示了给定的图表：
#
#红色显示的边是桥。其中有四条。
#
#输入样本 2
#3 3
#1 2
#1 3
#2 3
#
#样本输出2
#0
#有可能是没有桥。
#
#样本输入3
#6 5
#1 2
#2 3
#3 4
#4 5
#5 6
#
#样本输出 3
#5
#有可能每条边都是桥。

def 