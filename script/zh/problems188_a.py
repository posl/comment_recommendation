#问题陈述
#一场篮球比赛正在进行中，现在的比分是X-Y。这里，可以保证X≠Y。
#落后的一方能否用一个成功的三分球扭转局面？
#换句话说，如果落后的一队获得三分，其分数是否会严格地大于另一队的分数？  
#
#限制条件
#0 ≦ X ≦ 100
#0 ≦ Y ≦ 100
#X ≠ Y
#X和Y是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#X Y
#
#输出
#如果落后的球队能用一个成功的三分球扭转局面，打印Yes；否则，打印No。
#
#输入样本 1
#3 5
#
#输出示例 1
#是
#得3分的球队落后。
#在一个成功的3分球后，它将有6分，这比另一队的5分要多。
#因此，我们应该打印Yes。
#
#输入样本 2
#16 2
#
#样本输出2
#不
#差距太大。落后的球队不能通过获得3分而超越对方。  
#
#输入样本 3
#12 15
#
#采样输出3
#不
#一个3分球可以追平比分，但不能扭转局面。

def 