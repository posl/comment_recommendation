#问题陈述
#Joisino在一家剧院担任接待员。
#剧院有100000个座位，编号从1到100000。
#根据她的备忘录，目前已有N组观众前来观看，第i组观众占据了从座位l_i到座位r_i（含）的连续座位。
#现在有多少人坐在剧院里？
#
#约束条件
#1≤N≤1000
#1≤l_i≤r_i≤100000
#没有一个座位被一个以上的人占据。
#所有的输入值都是整数。
#
#输入
#输入是由标准输入给出的，格式如下：
#N
#l_1 r_1
#:
#l_N r_N
#
#输出
#打印坐在剧院里的人数。
#
#输入样本 1
#1
#24 30
#
#样本输出1
#7
#有7个人，坐在24、25、26、27、28、29和30号座位上。
#
#样本输入2
#2
#6 8
#3 3
#
#样本输出2
#4

def 