#问题陈述
#给你N个编号为1到N的区间，这些区间的情况如下：
#如果t_i=1，区间i是[l_i,r_i]；
#如果t_i=2，区间i是[l_i,r_i]；
#如果t_i=3，则区间i为（l_i,r_i）；
#如果t_i=4，区间i是(l_i,r_i)。
#有多少对满足1 ≦ i < j ≦ N的整数(i,j)可以使区间i和区间j相交？
#什么是[X,Y],[X,Y],(X,Y)?
#闭合区间[X,Y]是由所有实数x组成的区间，使得X ≦ x ≦ Y。
#半开区间[X,Y]是一个由所有实数x组成的区间，使得X ≦ x < Y。
#半开区间(X,Y)是一个由所有实数x组成的区间，使得X < x ≦ Y。
#一个开放区间(X,Y)是一个由所有实数x组成的区间，使得X < x < Y。
#粗略地说，方括号[]意味着端点被包括在内，而大括号（）意味着端点被排除。
#
#限制条件
#2 ≦ N ≦ 2000
#1 ≦ t_i ≦ 4
#1 ≦ l_i < r_i ≦ 10^9
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#N
#t_1 l_1 r_1
#t_2 l_2 r_2
#.
#.
#.
#t_N l_N r_N
#
#输出
#打印有多少对整数(i,j)使区间i和区间j相交。
#
#输入样本 1
#3
#1 1 2
#2 2 3
#3 2 4
#
#样本输出 1
#2
#根据问题陈述的定义，区间1是[1,2]，区间2是[2,3]，区间3是（2,4）。
#有两对整数（i,j）使区间i和区间j相交：（1,2）和（2,3）。对于第一对，交点是[2,2]，对于第二对，交点是(2,3)。
#
#样本输入2
#19
#4 210068409 221208102
#4 16698200 910945203
#4 76268400 259148323
#4 370943597 566244098
#1 428897569 509621647
#4 250946752 823720939
#1 642505376 868415584
#2 619091266 868230936
#2 306543999 654038915
#4 486033777 715789416
#1 527225177 583184546
#2 885292456 900938599
#3 264004185 486613484
#2 345310564 818091848
#1 152544274 521564293
#4 13819154 555218434
#3 507364086 545932412
#4 797872271 935850549
#2 415488246 685203817
#
#样本输出2
#102

def 