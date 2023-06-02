#问题陈述
#有N块寿司。每一块都有两个参数："配料的种类 "t_i和 "美味程度 "d_i。
#你要在这N块中选择K块来吃。
#你在这里的 "满意度 "将被计算如下：
#满意度是 "基本总美味 "和 "品种奖励 "的总和。
#基本总美味是你所吃的各块的美味之和。
#种类奖励是x*x，其中x是你吃的不同种类的配料的数量。
#你希望有尽可能多的满足感。
#找到这个最大的满意度。
#
#约束条件
#1 ≦ k ≦ n ≦ 10^5
#1 ≦ t_i ≦ N
#1 ≦ d_i ≦ 10^9
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#N K
#t_1 d_1
#t_2 d_2
#.
#.
#.
#t_N d_N
#
#输出
#打印你能获得的最大满意度。
#
#输入样本 1
#5 3
#1 9
#1 7
#2 6
#2 5
#3 1
#
#样本输出1
#26
#如果你吃了寿司1,2和3：
#基本总美味是9+7+6=22。
#种类奖励是2*2=4。
#因此，你的满意度将是26，这是最佳的。
#
#输入样本 2
#7 4
#1 1
#2 1
#3 1
#4 6
#4 5
#4 5
#4 5
#
#样本输出2
#25
#吃寿司1,2,3和4是最佳选择。
#
#样本输入3
#6 5
#5 1000000000
#2 990000000
#3 980000000
#6 970000000
#6 960000000
#4 950000000
#
#样本输出3
#4900000016
#注意，输出可能不适合32位整数类型。

def 