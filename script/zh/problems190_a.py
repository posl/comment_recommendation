#问题陈述
#高桥和青木将进行一场对战游戏。
#最初，高桥和青木分别有A和B的糖果。
#他们将交替进行以下操作。如果C=0，高桥先做，如果C=1，青木先做。
#吃下他手中的一颗糖果。
#先不能做操作的人就输了。哪个人将会赢？
#
#限制条件
#输入的所有数值都是整数。
#0≤A，B≤100
#C在{0, 1}中
#
#输入
#输入是由标准输入给出的，格式如下：
#A B C
#
#輸出
#如果高桥会赢，打印高桥；如果青木会赢，打印青木。
#
#输入样本 1
#2 1 0
#
#样本输出 1
#高桥
#最初，高桥和青木分别有2个和1个糖果（ies）。
#游戏将按以下方式进行：
#高桥吃他的糖果。
#青木吃他的糖果。
#高桥吃了他的糖果。
#青木没有更多的糖果了，所以高桥获胜。
#
#输入样本 2
#2 2 0
#
#样本输出 2
#青木
#
#样本输入3
#2 2 1
#
#样本输出3
#高桥

def 