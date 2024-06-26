#问题陈述
#两只狐狸Jiro和Saburo正在玩一种叫做1D Reversi的游戏。这个游戏是在一个棋盘上进行的，使用黑色和白色的石头。在棋盘上，石子被摆成一排，每个玩家在这排的两端各放一块新石子。与最初的黑白棋游戏类似，当放置一颗白棋时，新的白棋和另一颗白棋之间的所有黑棋都会变成白棋，反之亦然。
#在游戏的中间，出现了一些情况，三郎不得不离开游戏。棋盘上有|S|（S的长度）个棋子，S中的每个字符代表左边第i（1 ≦ i ≦ |S|）个棋子的颜色。如果S中的第i个字符是B，这意味着棋盘上相应的石头的颜色是黑色。同样地，如果S中的第i个字符是W，意味着对应的石头的颜色是白色。
#二郎希望棋盘上的所有棋子都是相同的颜色。为此，他将根据规则在棋盘上放置新的棋子。请找出他需要放置的最小数量的新石子。
#
#限制条件
#1 ≦ |S| ≦ 10^5
#S中的每个字符都是B或W。
#
#输入
#输入来自标准输入，格式如下：
#S
#
#输出
#打印二郎需要放置的最小数量的新石头，以达到他的目的。
#
#输入样本1
#BBBWW
#
#样本输出1
#1
#在这一排棋子的右端放一个新的黑棋，所有的白棋就会变成黑棋。另外，在这排棋子的左端放一个新的白棋，所有的黑棋都会变成白棋。
#无论哪种方式，二郎的目的都可以通过放置一块石头来实现。
#
#输入样本2
#WWWWWWW
#
#样本输出2
#0
#如果所有的石头都已经是相同的颜色，就不需要新的石头了。
#
#样本输入3
#WBWBWBWBWB
#
#样本输出3
#9

def 