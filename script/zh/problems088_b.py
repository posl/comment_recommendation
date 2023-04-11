#问题陈述
#我们有N张卡片。在第i张卡片上写着一个数字a_i。
#爱丽丝和鲍勃将用这些卡片玩一个游戏。在这个游戏中，Alice和Bob轮流拿一张牌。爱丽丝先走。
#当两个玩家拿完所有的牌时，游戏就结束了，每个玩家的分数是写在他/她所拿的牌上的数字之和。当两个玩家都采取最优策略使他们的分数最大化时，求爱丽丝的分数减去鲍勃的分数。
#
#限制条件
#N是1到100（含）之间的整数。
#a_i (1 ≦ i ≦ N) 是1到100之间的整数（包括在内）。
#
#输入
#输入由标准输入提供，格式如下：  
#N
#a_1 a_2 a_3 ... a_N
#
#输出
#打印Alice的分数减去Bob的分数，当两个玩家都采取最优策略使他们的分数最大化。
#
#输入样本 1
#2
#3 1
#
#样品输出1
#2
#首先，爱丽丝拿的是3的牌，然后，鲍勃拿的是1的牌。
#他们的分数之差将是3-1=2。
#
#输入样本2
#3
#2 7 4
#
#样本输出2
#5
#首先，爱丽丝拿的是7的牌，然后，鲍勃拿的是4的牌，最后，爱丽丝拿的是2的牌，他们的分数差是7-4+2=5。他们的分数之差是3-1=2。
#
#输入样本 3
#4
#20 18 2 18
#
#样本输出3
#18

def 