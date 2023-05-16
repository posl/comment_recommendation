#问题陈述
#Fennec正在与N个怪兽战斗。
#第i个怪物的健康状况为H_i。
#Fennec可以做以下两个动作：
#攻击：Fennec选择一个怪物。该怪物的生命值将减少1。
#特殊动作：Fennec选择一只怪物。该怪物的生命值将变为0。
#除了攻击和特殊移动之外，没有其他方法可以减少怪物的生命值。
#当所有怪物的生命值都变成0或低于0时，Fennec获胜。
#当Fennec最多可以使用特殊动作K次时，找出Fennec在获胜前需要进行攻击（不算特殊动作）的最少次数。
#
#限制条件
#1 ≦ N ≦ 2 × 10^5
#0 ≦ K ≦ 2 × 10^5
#1 ≦ H_i ≦ 10^9
#输入的所有数值都是整数。
#
#输入
#输入由标准输入提供，格式如下：
#N K
#H_1 ...H_N
#
#输出
#打印Fennec在获胜前需要进行的最小攻击次数（不计入特殊移动）。
#
#输入样本 1
#3 1
#4 1 5
#
#样本输出 1
#5
#通过对第三只怪物使用特殊移动，对第一只怪物进行四次攻击，对第二只怪物进行一次攻击，芬尼克可以用五次攻击获胜。
#
#输入样本2
#8 9
#7 9 3 2 3 8 4 6
#
#样本输出2
#0
#她可以对所有的怪兽使用特殊动作。
#
#输入样本3
#3 0
#1000000000 1000000000 1000000000
#
#样本输出3
#3000000000
#注意溢出。

def 