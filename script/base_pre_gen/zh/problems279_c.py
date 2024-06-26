#问题陈述
#给你一个由#和.组成的模式S和T，每个模式有H行和W列。
#模式S是由H个字符串组成的，S_i的第j个字符代表第i行和第j列中的元素。T的情况也是如此。
#判断是否可以通过重新排列S的列来使S等于T。
#这里，重新排列一个图案X的列的方法如下。
#选择一个(1,2,...,W)的排列组合P=(P_1,P_2,...,P_W)。
#然后，对于每一个整数i，如1 ≦ i ≦ H，同时做以下工作。
#对于每个整数j，如1 ≦ j ≦ W，同时将X的第i行和第j列的元素替换为第i行和第P_j列的元素。
#
#
#限制条件
#H和W是整数。
#1 ≦ H,W
#1 ≦ H × W ≦ 4 × 10^5
#S_i和T_i是长度为W的字符串，由#和.组成。
#
#输入
#输入是由标准输入给出的，格式如下：
#H W
#S_1
#S_2
#.
#.
#.
#S_H
#T_1
#T_2
#.
#.
#.
#T_H
#
#输出
#如果S可以与T相等，则打印Yes；否则，打印No。
#
#输入样本 1
#3 4
###.#
###..
##...
#.###
#..##
#...#
#
#样本输出1
#是的
#例如，如果你把S的第3列、第4列、第2列和第1列按这个顺序从左到右排列，S将等于T。
#
#输入样本2
#3 3
##.#
#.#.
##.#
###.
###.
#.#.
#
#样本输出2
#不
#在这个输入中，不能使S等于T。
#
#样本输入3
#2 1
##
#.
##
#.
#
#样本输出3
#是
#有可能是S=T。
#
#样本输入4
#8 7
##..#..#
#.##.##.
##..#..#
#.##.##.
##..#..#
#.##.##.
##..#..#
#.##.##.
#....###
#####...
#....###
#####...
#....###
#####...
#....###
#####...
#
#样本输出4
#是

def 