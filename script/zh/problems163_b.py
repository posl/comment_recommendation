#问题陈述
#高桥有N天的暑假。
#他的老师给他布置了M项暑假作业。他需要A_i天来完成第i项作业。
#他不能在同一天做多项作业，也不能在做作业的当天出去玩。
#如果高桥在这个假期中完成所有的作业，那么他在假期中最多可以出去玩多少天？
#如果高桥在假期中不能完成所有的作业，则打印-1。
#
#限制条件
#1 ≦ N ≦ 10^6
#1 ≦ M ≦ 10^4
#1 ≦ A_i ≦ 10^4
#
#输入
#输入是由标准输入法提供的，格式如下：
#N M
#A_1 ...A_M
#
#输出
#打印高桥在假期中最多可以游玩的天数，或-1。
#
#输入样本 1
#41 2
#5 6
#
#样本输出1
#30
#例如，他可以在头5天做第一项任务，在接下来的30天里闲逛，并在假期的最后6天做第二项任务。这样一来，他可以安全地花30天时间出去玩。
#
#输入样本2
#10 2
#5 6
#
#样本输出2
#-1
#他不能完成他的作业。
#
#输入样本3
#11 2
#5 6
#
#样本输出3
#0
#他可以完成他的作业，但他将没有时间出去玩。
#
#样本输入4
#314 15
#9 26 5 35 8 9 79 3 23 8 46 2 6 43 3
#
#样本输出 4
#9

def 