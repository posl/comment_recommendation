#问题陈述
#有三个机场A、B和C，每对机场之间都有双向的航班。
#A机场和B机场之间的单程飞行需要P小时，B机场和C机场之间的单程飞行需要Q小时，C机场和A机场之间的单程飞行需要R小时。
#考虑一条路线，我们从其中一个机场出发，飞到另一个机场，然后再飞到另一个机场。
#可能的最小飞行时间之和是多少？
#
#限制条件
#1 ≦ p,q,r ≦ 100
#输入的所有数值都是整数。
#
#输入
#输入由标准输入提供，格式如下：
#P Q R
#
#输出
#打印最小可能的飞行时间之和。
#
#输入样本 1
#1 3 4
#
#样本输出 1
#4
#A->B->C路线的飞行时间之和：1+3=4小时
#航线A->C->C的飞行时间之和：4+3=7小时
#航线B->A->C的飞行时间之和：1+4=5小时
#B->C->A航线的飞行时间之和：3+4=7小时
#航线C->A->B的飞行时间之和：4+1=5小时
#航线C->B->A的飞行时间之和：3+1=4小时
#其中最小的是4小时。
#
#输入样本 2
#3 2 3
#
#样本输出 2
#5

def 