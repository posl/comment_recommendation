#问题陈述
#高桥有一个迷宫，它是一个由H×W个方块组成的网格，有H个横行和W个纵列。
#如果S_{ij}是#，位于从顶部第i行和第j列的方格是 "墙 "方格，如果S_{ij}是.，则是 "路 "方格。
#从一个道路方格，你可以移动到一个水平或垂直相邻的道路方格。
#你不能移出迷宫，不能移到墙上的方格，也不能斜向移动。
#高桥将选择一个起始方格和一个目标方格，可以是任何道路方格，并将迷宫交给青木。
#然后，青木将在所需的最小移动数内从起点方格走到目标方格。
#在这种情况下，请找出Aoki所要走的最大可能的步数。
#
#限制条件
#1 ≦ H,W ≦ 20
#S_{ij}是.或#。
#S中至少有两次出现.的情况。
#任何一个道路方块都可以在零或更多的移动中从任何道路方块到达。
#
#输入
#输入是由标准输入法提供的，其格式如下：
#H W
#S_{11}...S_{1W}。
#:
#s_{h1}...s_{hw}。
#
#输出
#打印Aoki所要下的最大可能的棋步数。
#
#输入样本 1
#3 3
#...
#...
#...
#
#样本输出1
#4
#如果高桥选择左上角的方格作为起始方格，右下角的方格作为目标方格，那么青木必须下四步棋。
#
#输入样本2
#3 5
#...#.
#.#.#.
#.#...
#
#样本输出2
#10
#如果高桥选择左下角的方格作为起始方格，右上角的方格作为目标方格，那么青木必须下十步棋。

def 