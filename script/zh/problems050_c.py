#问题陈述
#有N个人，方便地编号为1到N。
#他们昨天站成一排，但现在他们不确定自己的站位顺序。
#然而，每个人都记得以下事实：站在该人左边的人的人数与站在该人右边的人的人数的绝对差。
#根据他们的报告，第i个人的上述差额为A_i。
#根据这些报告，找出他们所站的可能顺序的数目。
#由于它可能非常大，请将答案以10^9+7为模数打印出来。
#请注意，这些报告可能是不正确的，因此可能没有一致的顺序。
#在这种情况下，打印0。
#
#限制条件
#1≦N≦10^5
#0≦A_i≦N-1
#
#输入
#输入由标准输入提供，格式如下：
#N
#A_1 A_2 ...A_N
#
#输出
#打印他们可能站立的顺序的数量，模数为10^9+7。
#
#输入样本1
#5
#2 4 4 0 2
#
#样本输出1
#4
#有四个可能的顺序，如下所示：
#2,1,4,5,3
#2,5,4,1,3
#3,1,4,5,2
#3,5,4,1,2
#
#样本输入2
#7
#6 4 0 2 4 0 2
#
#样本输出2
#0
#任何顺序都会与报告不一致，因此答案是0。
#
#样本输入3
#8
#7 5 1 1 7 3 5 3
#
#样本输出3
#16

def 