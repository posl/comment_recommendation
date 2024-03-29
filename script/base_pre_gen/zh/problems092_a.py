#问题陈述
#你计划利用火车和公共汽车进行一次旅行。
#如果你沿途购买普通车票，火车票价为A日元（日本的货币），如果你购买无限期车票，则为B日元。
#同样，如果你沿途购买普通车票，公共汽车的票价将是C日元，如果你购买无限期车票，则是D日元。
#当对火车和公共汽车作出最佳选择时，找出最低总票价。
#
#限制条件
#1 ≦ A ≦ 1 000
#1 ≦ B ≦ 1 000
#1 ≦ C ≦ 1 000
#1 ≦ D ≦ 1 000
#所有输入值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#A
#B
#C
#D
#
#输出
#打印最低总票价。
#
#输入样本1
#600
#300
#220
#420
#
#样本输出1
#520
#如果你购买普通车票，火车票价为600日元，如果你购买无限期车票，则为300日元。
#因此，火车的最佳选择是购买300日元的无限期票。
#另一方面，公共汽车的最佳选择是购买220日元的普通票。
#因此，最低总票价为300+220=520日元。
#
#输入样本2
#555
#555
#400
#200
#
#样本输出2
#755
#
#样本输入3
#549
#817
#715
#603
#
#样本输出3
#1152

def 