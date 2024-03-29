#问题陈述
#有一个二维平面。对于1到9之间的整数r和c，如果S_{r}的第c个字符是#，则在坐标(r,c)处有一个卒，如果S_{r}的第c个字符是...，则没有卒。
#求该平面内四个顶点都有棋子的方格数。
#
#限制条件
#S_1,...,S_9中的每一个都是一个长度为9的字符串，由#和...组成。
#
#输入
#输入来自标准输入，其格式如下：
#S_1
#S_2
#.
#.
#.
#S_9
#
#输出
#打印答案。
#
#输入样本1
###.......
###.......
#.........
#.......#.
#.....#...
#........#
#......#..
#.........
#.........
#
#样本输出1
#2
#顶点为(1,1)、(1,2)、(2,2)和(2,1)的正方形在所有四个顶点上都有棋子。
#顶点为(4,8)、(5,6)、(7,7)和(6,9)的广场也在所有四个顶点上都有棋子。
#因此，答案是2。
#
#输入样本2
#.#.......
##.#......
#.#.......
#.........
#....#.#.#
#.........
#....#.#.#
#........#
#.........
#
#样本输出2
#3

def 