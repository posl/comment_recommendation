#问题陈述
#有一个横排为H，竖排为W的网格。  (i, j)表示位于从上往下第i行和从左往下第j列的方格。
#N个方格，（r_1，c_1），（r_2，c_2），...，（r_N，c_N），都有墙。
#高桥最初在(r_s, c_s)广场。
#给予高桥的指令是Q。
#对于i=1，2，...，Q，第i条指令由一对字符d_i和一个正整数l_i表示。d_i是L、R、U和D中的一个，分别代表左、右、上、下的方向。
#给定第i个方向，高桥重复以下动作l_i次：
#如果在d_i所代表的方向上，有一个没有墙的方块与当前方块相邻，则移动到该方块；
#否则，什么也不做。
#对于i=1，2，...，Q，打印出高桥在遵循前i条指令后将所在的方格。
#
#限制条件
#2 ≦ h, w ≦ 10^9
#1 ≦ r_s ≦ H
#1 ≦ c_s ≦ W
#0 ≦ N ≦ 2 × 10^5
#1 ≦ r_i ≦ H
#1 ≦ c_i ≦ W
#i ≠ j -> (r_i, c_i) ≠ (r_j, c_j)
#(r_s, c_s) ≠ (r_i, c_i) 对于所有i = 1, 2, ..., N。
#1 ≦ Q ≦ 2 × 10^5
#d_i是L、R、U和D中的一个字符。
#1 ≦ l_i ≦ 10^9
#输入中除d_i以外的所有数值都是整数。
#
#输入
#输入来自标准输入，格式如下：
#H W r_s c_s
#N
#r_1 c_1
#r_2 c_2
#.
#.
#.
#r_N c_N
#Q
#d_1 l_1
#d_2 l_2
#.
#.
#.
#d_Q l_Q
#
#输出
#打印Q行。
#对于i=1，2，...，Q，第i行应该包含高桥在遵循第一个i指令后的方格（R_i，C_i），格式如下：
#R_1 C_1
#R_2 C_2
#.
#.
#.
#R_Q C_Q
#
#样本输入1
#5 5 4 4
#3
#5 3
#2 2
#1 4
#4
#L 2
#U 3
#L 2
#R 4
#
#样品输出1
#4 2
#3 2
#3 1
#3 5
#给定的网格和高桥的初始位置如下，其中#表示有墙的方块，T表示高桥所在的方块，.表示其他方块：
#...#.
#.#...
#.....
#...T.
#..#..
#给出第1条指令，高桥向左移动2个格子，最后停留在(4, 2)格子上，如下所示：
#...#.
#.#...
#.....
#.T...
#..#..
#根据第2条指令，高桥首先向上移动了1个方格，然后他 "什么都不做 "了两次，因为在他的方向相邻的方格有一堵墙。  结果，他最终在(3, 2)号格子里，情况如下：
#...#.
#.#...
#.T...
#.....
#..#..
#在第3条指令下，高桥首先向左移动1个方格，然后他 "什么都不做 "一次，因为在他的方向没有方格。  结果，他最后在(3, 1)方格，如下所示：
#...#.
#.#...
#T....
#.....
#..#..
#给出第4条指令，高桥向右移动4个格子，最后在(3, 5)格子里，如下所示：
#...#.
#.#...
#....T
#.....
#..#..
#
#输入样本2
#6 6 6 3
#7
#3 1
#4 3
#2 6
#3 4
#5 5
#1 1
#3 2
#10
#D 3
#U 3
#L 2
#D 2
#U 3
#D 3
#U 3
#R 3
#L 3
#D 1
#
#样本输出 2
#6 3
#5 3
#5 1
#6 1
#4 1
#6 1
#4 1
#4 2
#4 1
#5 1

def 