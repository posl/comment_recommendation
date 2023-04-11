#问题陈述
#我们有一个H×W的网格，其方格被涂成黑色或白色。位于从上往下第i行和从左往下第j列的方格被称为（i，j）。
#Snuke想在这个网格上玩以下游戏。在游戏开始时，在（1，1）方格有一个叫Kenus的角色。玩家重复地将Kenus向上、向下、向左或向右移动一个方格。当Kenus到达（H，W）方格时，只通过白色方格，游戏就结束了。
#在Snuke开始游戏之前，他可以将一些白色方格的颜色改为黑色。但是，他不能改变（1，1）和（H，W）方格的颜色。另外，颜色的改变必须在游戏开始前全部进行。
#游戏结束后，Snuke的得分将是他在游戏开始前改变一个方格颜色的次数。找出斯努克可能达到的最高分数，如果游戏无法完成，即无论斯努克如何改变方格的颜色，凯努斯都无法到达（H，W）方格，则打印-1。  
#方格的颜色以字符s_{i, j}的形式给你。如果方格（i，j）最初被涂成白色，s_{i，j}就是.；如果方格（i，j）最初被涂成黑色，s_{i，j}就是#。
#
#限制条件
#H是2到50（包括）之间的整数。
#W是2到50（包括）之间的整数。
#s_{i, j}是.或#（1 ≦ i ≦ H, 1 ≦ j ≦ W）。
#s_{1, 1}和s_{H, W}是...。
#
#输入
#输入由标准输入提供，格式如下：
#H W
#s_{1, 1}s_{1, 2}s_{1, 3} ... s_{1, W}
#s_{2, 1}s_{2, 2}s_{2, 3} ... s_{2, W}
# : :
#s_{H, 1}s_{H, 2}s_{H, 3} ... s_{H, W}
#
#输出
#打印Snuke可能达到的最大分数，如果游戏无法完成，则打印-1。
#
#输入样本 1
#3 3
#..#
##..
#...
#
#输出样本 1
#2
#分数2可以通过改变方块的颜色来实现，如下所示：
#
#样本输入2
#10 37
#.....................................
#...#...####...####..###...###...###..
#..#.#..#...#.##....#...#.#...#.#...#.
#..#.#..#...#.#.....#...#.#...#.#...#.
#.#...#.#..##.#.....#...#.#.###.#.###.
#.#####.####..#.....#...#..##....##...
#.#...#.#...#.#.....#...#.#...#.#...#.
#.#...#.#...#.##....#...#.#...#.#...#.
#.#...#.####...####..###...###...###..
#.....................................
#
#样本输出2
#209

def 