#问题陈述
#在一条数线上有2000001个石头。这些石头的坐标是-1000000, -999999, -999998, ..., 999999, 1000000。
#在这些石头中，有一些连续的石头被涂成黑色，其他的被涂成白色。
#此外，我们知道坐标X处的石头被涂成了黑色。
#按升序打印所有可能包含涂成黑色的石头的坐标。
#
#限制条件
#1 ≦ K ≦ 100
#0 ≦ X ≦ 100
#输入的所有数值都是整数。
#
#输入
#输入由标准输入提供，其格式如下：
#K X
#
#输出
#打印所有可能包含涂成黑色的石头的坐标，按升序排列，中间有空格。
#
#输入样本 1
#3 7
#
#输出样本 1
#5 6 7 8 9
#我们知道有三块石头被涂成黑色，坐标7的石头被涂成黑色。有三种可能的情况：
#三块涂成黑色的石头被放在坐标5、6、7处。
#三块涂成黑色的石头被放在坐标6、7和8处。
#三个涂成黑色的石头被放在坐标7、8和9处。
#因此，有五个坐标可能包含一个黑色的石头：5、6、7、8和9。
#
#输入样本 2
#4 0
#
#输出样本 2
#-3 -2 -1 0 1 2 3
#负坐标也可以包含一个涂成黑色的石头。
#
#输入样本3
#1 100
#
#样本输出3
#100

def 