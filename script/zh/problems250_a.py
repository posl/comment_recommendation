#问题陈述
#有一个有H个水平行和W个垂直列的网格。让(i,j)表示从上往下第i行和从左往下第j列的正方形。
#求与正方形（R，C）共用一条边的正方形的数量。
#在这里，当且仅当|a-c|+|b-d|=1（其中|x|表示x的绝对值）时，两个正方形（a,b）和（c,d）被称为共享一个边。
#
#限制条件
#输入的所有数值都是整数。
#1 ≦ R ≦ H ≦ 10
#1 ≦ C ≦ W ≦ 10
#
#输入
#输入由标准输入提供，格式如下：
#H W
#R C
#
#輸出
#以整数形式打印答案。
#
#输入样本 1
#3 4
#2 2
#
#样品输出1
#4
#我们将在下面一次性描述样本输入/输出1,2和3，样本输出3。
#
#样本输入2
#3 4
#1 3
#
#样本输出2
#3
#
#样本输入 3
#3 4
#3 4
#
#样本输出 3
#2
#当H=3，W=4时，网格看起来如下。
#对于样本输入1，有4个方格与方格（2,2）相邻。
#对于样本输入2，有3个方格与方格（1,3）相邻。
#对于样本输入3，有2个方格与方格（3,4）相邻。
#
#
#样本输入4
#1 10
#1 5
#
#样本输出4
#2
#
#采样输入5
#8 1
#8 1
#
#样本输出 5
#1
#
#样本输入 6
#1 1
#1 1
#
#采样输出6
#0

def 