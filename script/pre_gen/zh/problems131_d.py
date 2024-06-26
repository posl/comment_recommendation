#问题陈述
#在AtCoder王国的国家问题研讨会上，Kizahashi被任命为ABC的管理员，他过于兴奋，承担了太多的工作。
#设当前时间为0，Kizahashi有N个工作，编号为1到N。
#Kizahashi完成工作i需要A_i单位的时间。工作i的最后期限是时间B_i，他必须在这个时间之前或之前完成工作。
#Kizahashi不能同时进行两项或多项工作，但当他完成一项工作后，可以立即开始进行另一项工作。
#Kizahashi能及时完成所有的工作吗？如果他能，请打印 "Yes"；如果他不能，请打印 "No"。
#
#限制条件
#输入的所有数值都是整数。
#1 ≦ N ≦ 2 × 10^5
#1 ≦ A_i, B_i ≦ 10^9 (1 ≦ i ≦ N)
#
#输入
#输入是由标准输入提供的，格式如下：
#N
#A_1 B_1
#.
#.
#.
#A_N B_N
#
#输出
#如果Kizahashi能及时完成所有工作，打印Yes；如果他不能，打印No。
#
#输入样本1
#5
#2 4
#1 9
#1 8
#4 9
#3 12
#
#样本输出1
#Yes
#他可以按时完成所有的工作，例如，按以下顺序做这些工作：
#从时间0到1做工作2。
#从时间1到3做工作1。
#从时间3到7做工作4。
#从时间7到8做工作3。
#做工作5，从时间8到11。
#请注意，在最后期限，即时间8完成工作3是可以的。
#
#输入样本2
#3
#334 1000
#334 1000
#334 1000
#
#样本输出2
#No
#他不能及时完成所有的工作，无论他以何种顺序做这些工作。
#
#输入样本3
#30
#384 8895
#1725 9791
#170 1024
#4 11105
#2 6
#578 1815
#702 3352
#143 5141
#1420 6980
#24 1602
#849 999
#76 7586
#85 5570
#444 4991
#719 11090
#470 10708
#1137 4547
#455 9003
#110 9901
#15 8578
#368 3692
#104 1286
#3 4
#366 12143
#7 6649
#610 2374
#152 7324
#4 7042
#292 11386
#334 5720
#
#样本输出3
#Yes

def 