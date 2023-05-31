#问题陈述
#AtCoder共和国位于一个笛卡尔坐标平面上。
#它有N个城镇，编号为1，2，...，N。城镇i位于（x_i，y_i），没有两个不同的城镇位于相同的坐标。
#这个国家有传送法术。一个法术由一对整数(a,b)标识，在坐标(x,y)处施展法术(a,b)可以将你传送到(x+a, y+b)。
#斯努克是一个伟大的魔术师，他可以为他选择的任何一对整数（a，b）学习咒语（a，b）。他能学习的法术数量也是无限的。
#为了能够使用法术在城镇之间旅行，他决定学习一定数量的法术，这样就有可能对每一对不同的城镇（i，j）做以下事情。
#在所学的法术中只选择一个法术。然后，反复使用所选的法术，从i镇到j镇。
#Snuke至少需要学习多少个法术才能实现上述目标？
#
#限制条件
#2 ≦ N ≦ 500
#0 ≦ x_i ≦ 10^9 (1 ≦ i ≦ N)
#0 ≦ y_i ≦ 10^9 (1 ≦ i ≦ N)
#(x_i, y_i) ≠ (x_j, y_j) if i ≠ j.
#
#输入
#输入由标准输入提供，格式如下：
#N
#x_1 y_1
#x_2 y_2
#.
#.
#.
#x_N y_N
#
#输出
#打印Snuke需要学习的最小法术数。
#
#输入样本 1
#3
#1 2
#3 6
#7 4
#
#样本输出1
#6
#下图说明了城镇的位置（以及四个角的坐标）。
#如果Snuke学会了下面的六个法术，他可以通过对每一对(i,j)(i≠j)使用一次法术，从城镇i到城镇j，实现他的目标。
#(2, 4)
#(-2, -4)
#(4, -2)
#(-4, 2)
#(-6, -2)
#(6, 2)
#另一个选择是学习下面的六个法术。在这种情况下，他可以通过对每一对(i,j)(i ≠ j)使用其中一个法术两次来从i镇到j镇，实现他的目标。
#(1, 2)
#(-1, -2)
#(2, -1)
#(-2, 1)
#(-3, -1)
#(3, 1)
#没有一个法术组合是由少于6个法术组成并达到目的的，所以我们应该打印6。
#
#输入样本 2
#3
#1 2
#2 2
#4 2
#
#样本输出 2
#2
#最佳选择是学习下面两个咒语：
#(1, 0)
#(-1, 0)
#
#样本输入 3
#4
#0 0
#0 1000000000
#1000000000 0
#1000000000 1000000000
#
#样本输出3
#8

def 