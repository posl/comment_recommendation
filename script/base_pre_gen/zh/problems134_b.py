#问题陈述
#一排有N棵苹果树。人们说，其中一棵会结出金苹果。
#我们想部署一定数量的检查员，以便对这些树中的每一棵进行检查。
#每个检查员将被部署在其中一棵树下。为方便起见，我们将给这些树分配从1到N的数字。部署在第i棵树下的检查员（1 ≦ i ≦ N）将检查编号在i-D和i+D（包括）之间的树。
#找到我们需要部署的检查员的最小数量以实现目标。
#
#约束条件
#输入的所有数值都是整数。
#1 ≦ N ≦ 20
#1 ≦ D ≦ 20
#
#输入
#输入由标准输入提供，格式如下：
#N D
#
#输出
#打印我们为实现目标所需部署的最小检查员数量。
#
#输入样本 1
#6 2
#
#样本输出 1
#2
#我们可以通过，例如，在树3和树4下放置一个检查员来实现这个目标。
#
#输入样本2
#14 3
#
#样本输出 2
#2
#
#采样输入3
#20 4
#
#样品输出3
#3

def 