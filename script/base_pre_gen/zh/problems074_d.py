#问题陈述
#在曾经存在的高桥王国，有N个城市，一些城市之间由道路双向连接。
#以下是关于道路网的已知信息：
#人们只通过公路在城市之间旅行。从任何其他城市到达任何城市都是可能的，必要时可以通过中间城市。
#不同的道路可能有不同的长度，但所有的长度都是正整数。
#考古学家斯努克在高桥王国的废墟中发现了一张有N行N列的表格，即A。
#他认为这代表了王国中沿路城市间的最短距离。
#确定是否存在一个道路网络，使得对于每个u和v，A的第u行和第v列的整数A_{u, v}等于从城市u到城市v的最短路径的长度。
#如果存在这样的网络，请找出可能的最短道路总长度。
#
#限制条件
#1 ≦ N ≦ 300
#如果i≠j，1 ≦ A_{i, j} = A_{j, i} ≦ 10^9。
#A_{i, i} = 0
#
#InputsInput由标准输入给出，格式如下：
#N
#A_{1, 1} A_{1, 2} ...A_{1, N}
#A_{2, 1} A_{2, 2} ...A_{2, N}
#...
#A_{N, 1} A_{N, 2} ...A_{N, N}
#
#输出
#如果不存在满足条件的网络，打印-1。
#如果存在，打印最短的道路总长度。
#
#输入样本 1
#3
#0 1 3
#1 0 2
#3 2 0
#
#样本输出1
#3
#下面的网络满足了这个条件：
#城市1和城市2由一条长度为1的道路连接。
#城市2和城市3由一条长度为2的道路连接。
#城市3和城市1之间没有道路连接。
#
#输入样本 2
#3
#0 1 3
#1 0 1
#3 1 0
#
#样本输出2
#-1
#由于从城市1到城市2和城市2到城市3有一条长度为1的路径，所以从城市1到城市3有一条长度为2的路径。
#然而，根据表格，城市1和城市3之间的最短距离必须是3。
#因此，我们得出结论，不存在满足条件的网络。
#
#样本输入3
#5
#0 21 18 11 28
#21 0 13 10 26
#18 13 0 23 13
#11 10 23 0 17
#28 26 13 17 0
#
#样本输出3
#82
#
#样本输入4
#3
#0 1000000000 1000000000
#1000000000 0 1000000000
#1000000000 1000000000 0
#
#样本输出4
#3000000000

def 