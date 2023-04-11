#问题陈述
#我们有一个有H行和W列的网格。位于第i行和第j列的方格将被称为Square（i,j）。
#从1到H×W的整数被写在整个网格中，写在方格（i,j）中的整数是A_{i,j}。
#你，一个神奇的女孩，可以通过消耗|x-i|+|y-j|魔法点数，将放置在广场（i,j）上的棋子传送到广场（x,y）。
#你现在必须参加Q的实际测试，以检验你作为魔法女孩的能力。
#第i次测试将按以下方式进行：
#最初，在写有整数L_i的广场上放一个棋子。
#设x是写在棋子所占方格中的整数。只要x不是R_i，就重复地将棋子移到写有整数x+D的方格。当x=R_i时，测试结束。
#在这里，可以保证R_i-L_i是D的倍数。
#对于每个测试，找出该测试期间消耗的魔力点的总和。
#
#约束条件
#1 ≦ H,W ≦ 300
#1 ≦ D ≦ H×W
#1 ≦ A_{i,j} ≦ H×W
#A_{i,j} ≠ A_{x,y} ((i,j) ≠ (x,y))
#1 ≦ Q ≦ 10^5
#1 ≦ L_i ≦ R_i ≦ H×W
#(R_i-L_i)是D的一个倍数。
#
#输入
#输入是由标准输入法提供的，其格式如下：
#H W D
#A_{1,1} A_{1,2} ...A_{1,W}
#:
#A_{H,1} A_{H,2} ...A_{H,W}
#Q
#L_1 R_1
#:
#L_Q R_Q
#
#输出
#对于每个测试，打印该测试期间消耗的魔力点的总和。
#输出应该按照测试的顺序进行。
#
#输入样本 1
#3 3 2
#1 4 3
#2 5 7
#8 9 6
#1
#4 8
#
#样本输出1
#5
#
#4被写在方格（1,2）中。
#6写在正方形(3,3)中。
#8被写在广场(3,1)上。
#因此，第一次测试时消耗的魔法点数之和为(|3-1|+|3-2|)+(|3-3|+|1-3|)=5。
#
#样本输入 2
#4 2 3
#3 7
#1 4
#5 2
#6 8
#2
#2 2
#2 2
#
#样本输出2
#0
#0
#请注意，可能有一个测试，棋子根本没有被移动，而且可能有多个相同的测试。
#
#输入样本 3
#5 5 4
#13 25 7 15 17
#16 22 20 2 9
#14 11 12 1 19
#10 6 23 8 18
#3 21 5 24 4
#3
#13 13
#2 10
#13 13
#
#样本输出3
#0
#5
#0

def 