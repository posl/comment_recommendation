#问题陈述
#我们有一个水平圆柱体。  给出Q个查询，按给定的顺序处理它们。
#每个查询都是以下两种类型中的一种。
#1 x c：在圆柱体的右端插入c个球，每个球上写有数字x。
#2 c:取出圆柱体中最左边的c个球，并打印出被取出的球上所写的数字之和。
#我们假设这些球在圆柱体中的顺序从未改变。
#
#限制条件
#1 ≦ Q ≦ 2× 10^5
#0 ≦ x ≦ 10^9
#1 ≦ c ≦ 10^9
#每当给出2 c类型的查询时，圆柱体中就有c个或更多的球。
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#Q
#query_1
#.
#.
#.
#query_Q
#第i个query_i是以下两种格式中的一种。
#1 x c
#2 c
#
#输出
#按给定的顺序打印对类型2 c的查询的响应，中间有换行。
#
#输入样本 1
#4
#1 2 3
#2 2
#1 3 4
#2 3
#
#样本输出1
#4
#8
#对于第一项查询，在圆柱体的右端插入3个球，每个球上都写有数字2。
#  圆柱体上的球从左到右都写有数字（2,2,2）。
#对于第2个问题，拿出圆柱体中最左边的两个球。
#  拿出的球上写的数字是2,2，总和是4，应该被打印出来。
#  现在圆柱体上有一个写有数字（2）的球，从左到右。
#对于第3个问题，在圆柱体的右端插入4个球，每个球上写有数字3。
#  现在圆柱体上的球从左到右写着数字（2,3,3,3,3）。
#在第4个问题中，取出圆柱体中最左边的3个球。
#  取出的球上写的数字是2,3,3，总和是8，应该被打印出来。
#  现在圆柱体上的球从左到右写着数字（3,3）。
#
#输入样本2
#2
#1 1000000000 1000000000
#2 1000000000
#
#样本输出2
#1000000000000000000
#
#样本输入3
#5
#1 1 1
#1 1 1
#1 1 1
#1 1 1
#1 1 1
#
#输出样本3
#可能没有什么你应该打印的。

def 