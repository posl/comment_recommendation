#问题陈述
#给你一个简单的无向图，有N个编号为1-N的顶点和M条编号为1-M的边。
#请找出该图中的连接部分的数量。
#
#注释
#一个简单的无定向图是一个简单的、有无定向边的图。
#当且仅当一个图没有自环或多边时，它就是简单的。
#一个图的子图是由该图的一些顶点和边形成的图。
#当且仅当人们可以通过边在每一对顶点之间旅行时，该图是连接的。
#连通组件是一个连通的子图，它不属于任何更大的连通子图。
#
#限制条件
#1 ≦ N ≦ 100
#0 ≦ m ≦ ((n(n - 1))/(2))
#1 ≦ u_i, v_i ≦ N
#给定的图形很简单。
#输入的所有数值都是整数。
#
#输入
#输入来自标准输入，其格式如下：
#N M
#u_1 v_1
#u_2 v_2
#.
#.
#.
#u_M v_M
#
#输出
#打印答案。
#
#输入样本 1
#5 3
#1 2
#1 3
#4 5
#
#样本输出 1
#2
#给定的图形包含以下两个连接部分：
#一个由顶点1，2，3和边1，2组成的子图；
#一个由顶点4、5和边3组成的子图。
#
#
#输入样本 2
#5 0
#
#样本输出2
#5
#
#样本输入3
#4 6
#1 2
#1 3
#1 4
#2 3
#2 4
#3 4
#
#样本输出3
#1

def 