#问题陈述
#高桥将A克黄金和B克白银（0≦A,B,0＜A+B）熔化并混合，以生产新的金属。
#他生产的是什么金属：纯金、纯银，还是合金？
#从形式上看，该产品被称为如下。
#纯金，如果0<A且B=0。
#纯银，如果A=0且0<B。
#合金，如果0<A和0<B。
#
#限制条件
#0 ≦ A,B ≦ 100
#1 ≦ A+B
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#A B
#
#输出
#如果产品是纯金，打印金；如果是纯银，打印银；如果是合金，打印合金。
#
#样品输入1
#50 50
#
#样品输出1
#合金
#我们有0<A和0<B，所以产品是一种合金。
#
#样本输入2
#100 0
#
#样本输出2
#黄金
#我们有0<A和B=0，所以产品是纯金。
#
#样本输入3
#0 100
#
#样本输出3
#银
#我们有A=0和0<B，所以产品是纯银。
#
#样本输入4
#100 2
#
#样品输出4
#合金

def 