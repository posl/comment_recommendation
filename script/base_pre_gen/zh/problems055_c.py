#问题陈述
#Snuke喜欢拼图。
#今天，他正在做一个使用S形和C形棋子的拼图。
#在这个谜题中，你可以将两个c形的棋子组合成一个S形的棋子，如下图所示：
#
#Snuke决定通过将一个S形的棋子和两个c形的棋子组合在一起，创造尽可能多的Scc组。
#当Snuke有N个S形棋子和M个C形棋子时，请找出可以创造的最大Scc组数。
#
#约束条件
#1 ≤ n,m ≤ 10^{12}。
#
#输入
#输入由标准输入提供，格式如下：
#N M
#
#输出
#打印答案。
#
#输入样本 1
#1 6
#
#样本输出 1
#2
#可以按以下方法创建两个Scc组：
#将两个c形片合并为一个S形片
#创建两个SCC组，每个组由一个S形片和两个C形片组成
#
#输入样本2
#12345 678901
#
#样本输出2
#175897

def 