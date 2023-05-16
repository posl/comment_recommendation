#问题陈述
#有N个人从西向东排队等候。
#给出的是一个长度为N的字符串S，代表人们的方向。
#如果S的第i个字符是L，那么从西边来的第i个人就朝向西边，如果S的这个字符是R，就朝向东边。
#如果在他/她前面的人朝向相同的方向，那么一个人是快乐的。
#然而，如果没有人站在一个人的前面，他/她就不快乐。
#你可以在0和K（包括）之间的任何次数进行以下操作：
#操作：选择整数l和r，使1 ≦ l ≦ r ≦ N，并将队列中的部分旋转180度：第l人，(l+1)-第，...，第r人。也就是说，对于每个i = 0, 1, ..., r-l，从西边来的第(l + i)-人在操作后将站在从西边来的第(r - i)-人，如果他/她现在面向西边，则面向东边，反之亦然。
#你能拥有的最大可能的幸福人数是多少？
#
#限制条件
#N是一个整数，满足1 ≦ N ≦ 10^5。
#K是一个整数，满足1 ≦ K ≦ 10^5。
#|S| = N
#S的每个字符都是L或R。
#
#输入
#输入是由标准输入法提供的，格式如下：
#N K
#S
#
#輸出
#打印最多经过K次操作后可能出现的最大快乐人数。
#
#输入样本 1
#6 1
#LRLRRL
#
#样本输出1
#3
#如果我们选择（l，r）=（2，5），我们有LLLRLL，其中来自西方的第2，3，6个人都很高兴。
#
#样本输入2
#13 3
#LRRLRLRRLLR
#
#采样输出2
#9
#
#样品输入3
#10 1
#LLLLLRRRRRR
#
#采样输出3
#9
#
#采样输入4
#9 2
#RRRLRLL
#
#采样输出4
#7

def 