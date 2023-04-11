#问题陈述
#有一个网格，从上到下有H行，从左到右有W列。让(i, j)表示从上往下第i行和从左往下第j列的方格。
#这些方块由字符C_{i,j}描述。如果C_{i,j}是.，（i，j）是空的；如果是#，（i，j）包含一个方块。
#对于满足1≦j≦W的整数j，让整数X_j定义如下。
#X_j是第j列中的盒子的数量。换句话说，X_j是整数i的数量，使得C_{i,j}是#。
#找到所有的X_1，X_2，...，X_W。
#
#限制条件
#1 ≦ H ≦ 1000
#1 ≦ W ≦ 1000
#H和W是整数。
#C_{i, j}是.或#。
#
#输入
#输入来自标准输入，其格式如下：
#H W
#C_{1,1}C_{1,2}...。C_{1,W}
#C_{2,1}C_{2,2}...C_{2,W}
#.
#.
#.
#C_{H,1}C_{H,2}...C_{H,W}
#
#输出
#按以下格式打印X_1, X_2, ..., X_W：
#X_1 X_2 ...X_W
#
#样本输入 1
#3 4
##..#
#.#.#
#.#.#
#
#样本输出1
#1 2 0 3
#在第1列中，有一个正方形（1，1），包含一个盒子。因此，X_1=1。
#在第2列中，两个方格（2，2）和（3，2）包含一个盒子。因此，X_2=2。
#在第3列中，没有方格包含一个盒子。因此，X_3=0。
#在第4列中，有三个方格（1，4）、（2，4）和（3，4）包含一个盒子。因此，X_4=3。
#因此，答案是（X_1, X_2, X_3, X_4）=（1, 2, 0, 3）。
#
#输入样本 2
#3 7
#.......
#.......
#.......
#
#样本输出2
#0 0 0 0 0 0 0
#可能没有包含盒子的方块。
#
#输入样本3
#8 3
#.#.
####
#.#.
#.#.
#.##
#..#
###.
#.##
#
#样本输出 3
#2 7 4
#
#样本输入4
#5 47
#.#..#..#####..#...#..#####..#...#...###...#####
#.#.#...#.......#.#...#......##..#..#...#..#....
#.##....#####....#....#####..#.#.#..#......#####
#.#.#...#........#....#......#..##..#...#..#....
#.#..#..#####....#....#####..#...#...###...#####
#
#输出样本 4
#0 5 1 2 2 0 0 5 3 3 3 3 0 0 1 1 3 1 1 0 0 5 3 3 3 3 0 0 5 1 1 1 5 0 0 3 2 2 2 2 0 0 5 3 3 3 3

def 