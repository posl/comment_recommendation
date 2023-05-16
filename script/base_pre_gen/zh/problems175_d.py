#问题陈述
#高桥将在一个编号为1，2，...，N的方格阵列上用棋子进行游戏。方格i上写有一个整数C_i。另外，他还得到了1, 2, ..., N的一个排列组合：P_1, P_2, ..., P_N。
#现在，他将选择一个方格并将棋子放在该方格上。然后，他将在1到K（包括）之间的一些次数进行下面的移动：
#在一步棋中，如果棋子现在在i方格（1 ≦ i ≦ N），就把它移到P_i方格。在这里，他的分数会增加C_{P_i}。
#帮助他找到对局结束时的最大可能分数。(在游戏开始时分数为0）。
#
#限制条件
#2 ≦ N ≦ 5000
#1 ≦ K ≦ 10^9
#1 ≦ P_i ≦ N
#P_i ≠ i
#P_1, P_2, ..., P_N 都是不同的。
#-10^9 ≦ C_i ≦ 10^9
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入给出的，格式如下：
#N K
#P_1 P_2 ...P_N
#C_1 C_2 ...C_N
#
#输出
#在游戏结束时打印出可能的最大分数。
#
#输入样本 1
#5 2
#2 4 5 1 3
#3 4 -10 -8 8
#
#样本输出1
#8
#当我们从我们选择的某个方格开始，并最多走两步棋时，我们有以下选择：
#如果我们从1号广场开始，走一步就把棋子送到2号广场，之后的分数是4。
#如果我们从方格2开始，走一步棋将棋子送到方格4，之后的分数是-8。再走一步棋将棋子送到方格1，之后的分数是-8+3=-5。
#如果我们从3号广场开始，走一步棋将棋子送到5号广场，之后的分数是8。再走一步棋将棋子送到3号广场，之后的分数是8+（-10）=-2。
#如果我们从方格4开始，走一步棋将棋子送到方格1，之后的分数是3。再走一步棋将棋子送到方格2，之后的分数是3+4=7。
#如果我们从5号广场开始，走一步棋会把棋子送到3号广场，之后的分数是-10。再走一步就把棋子送到5号方格，之后的分数是-10+8=-2。
#最高得分是8分。
#
#输入样本 2
#2 3
#2 1
#10 -7
#
#样本输出2
#13
#
#样本输入3
#3 3
#3 1 2
#-1000 -2000 -3000
#
#样本输出 3
#-1000
#我们至少要走一步。
#
#输入样本4
#10 58
#9 1 6 7 8 4 3 2 10 5
#695279662 988782657 -119067776 382975538 -151885171 -177220596 -169777795 37619092 389386780 980092719
#
#样本输出4
#29507023469
#答案的绝对值可能是巨大的。

def 