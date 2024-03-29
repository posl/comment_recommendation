#问题陈述
#有一个横排为H、竖排为W的网格，其中一些方格上有障碍物。
#斯努克要在没有障碍物的方格中选择一个方格，并在其上放置一盏灯。
#放在方格上的灯将向四个基本方向发出直光束：上、下、左、右。
#在每个方向上，光束都会继续移动，直到它碰到被障碍物占据的方格或碰到方格的边界。它将照亮沿途的所有方格，包括放置灯的方格，但不包括被障碍物占据的方格。
#Snuke希望最大化灯所照亮的方格数。
#如果S_i的第j个字符（1 ≦ j ≦ W）是#，则在从上往下第i行和从左往下第j列的方格上有一个障碍物；如果该字符是.，则该方格上没有障碍物。
#求灯所照亮的方格的最大可能数量。
#
#限制条件
#1 ≦ H ≦ 2,000
#1 ≦ W ≦ 2,000
#S_i是一个长度为W的字符串，由#和.
#.在其中一个字符串S_i中至少出现一次（1 ≦ i ≦ H）。
#
#输入
#输入是由标准输入提供的，格式如下：
#H W
#S_1
#:
#S_H
#
#输出
#打印该灯可能照亮的最大方格数。
#
#输入样本 1
#4 6
##..#..
#.....#
#....#.
##.#...
#
#样本输出1
#8
#如果Snuke将灯放在从上往下第二行和从左往下第二列的方格上，它将点亮以下方格：第二行中从左往下第一到第五个方格，以及第二列中从上往下第一到第四个方格，共八个方格。
#
#输入样本2
#8 8
#..#...#.
#....#...
###......
#..###..#
#...#..#.
###....#.
##...#...
####.#..#
#
#样本输出2
#13

def 