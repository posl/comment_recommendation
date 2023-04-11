#问题陈述
#我们有一个有H行和W列的方格。
#Snuke正在给这些方格涂上1，2，...，N的颜色。
#这里，应该满足以下条件：
#对于每一个i（1≤i≤N），正好有a_i个方格被涂成i色。+ a_N = H W。
#对于每一个i（1≤i≤N），涂在颜色i中的方块都是4个相连的。也就是说，每一个涂成i色的方块都可以从每一个涂成i色的方块出发，通过反复前往一个水平或垂直相邻的涂成i色的方块来到达。
#找到一种方法来涂抹这些方块，使其满足条件。
#可以证明，一个解决方案总是存在的。
#
#限制条件
#1 ≤ H, W ≤ 100
#1 ≤ N ≤ H W
#a_i ≥ 1
#a_1 + a_2 + ...+ a_N = H W
#
#输入
#输入是由标准输入给出的，格式如下：
#H W
#N
#a_1 a_2 ... a_N
#
#输出
#打印满足条件的方块的一种画法。
#输出
# 以下列格式输出：
#c_{1 1} ... c_{1 W}
#:
#c_{H 1} ... c_{H W}
#这里，c_{i j}是位于顶部第i行和左侧第j列的方块的颜色。
#
#输入样本 1
#2 2
#3
#2 1 1
#
#样本输出 1
#1 1
#2 3
#下面是一个无效的解决方案的例子：
#1 2
#3 1
#这是因为颜色1中的方块不是4个相连的。
#
#输入样本 2
#3 5
#5
#1 2 3 4 5
#
#样本输出 2
#1 4 4 4 3
#2 5 4 5 3
#2 5 5 5 3
#
#样本输入3
#1 1
#1
#1
#
#样本输出3
#1

def 