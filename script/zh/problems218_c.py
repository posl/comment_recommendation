#问题陈述
#在一个有正方形单元格的二维网格上，我们有两个图形S和T。
#S位于一个有N行N列的网格中，由S_{i,j}为#的单元格组成。
#T位于同一个有N行N列的网格中，由T_{i,j}为#的单元格组成。
#判断是否有可能通过90度的旋转和平移使S和T完全匹配。
#
#约束条件
#1 ≦ N ≦ 200
#S和T中的每一个都由#和.组成。
#S和T中的每一个都至少包含一个#。
#
#输入
#输入由标准输入提供，格式如下：
#N
#S_{1,1}S_{1,2}...S_{1,N}
#.
#.
#.
#S_{N,1}S_{N,2}...S_{N,N}
#T_{1,1}T_{1,2}...T_{1,N}
#.
#.
#.
#T_{N,1}T_{N,2}...T_{N,N}
#
#输出
#如果通过90度的旋转和平移可以完全匹配S和T，则打印Yes，否则打印No。
#
#输入样本 1
#5
#.....
#..#..
#.###.
#.....
#.....
#.....
#.....
#....#
#...##
#....#
#
#样本输出1
#是的
#我们可以通过逆时针旋转90度和平移，将S与T匹配。
#
#样本输入2
#5
######
###..#
##..##
######
#.....
######
##..##
###..#
######
#.....
#
#样本输出2
#不
#不可能通过90度的旋转和平移来匹配它们。
#
#输入样本3
#4
##...
#..#.
#..#.
#....
##...
##...
#..#.
#....
#
#样本输出3
#是
#S和T中的每一个都可能没有连接。
#
#采样输入4
#4
##...
#.##.
#..#.
#....
###..
##...
#..#.
#....
#
#样本输出4
#不
#注意，不允许只旋转或平移一个图形的一部分；只允许旋转或平移整个图形。

def 