#问题说明
#有N个球放在一排。
#小鹿AtCoDeer正在用他的油漆罐中的K种颜色给每个球上色。
#为了美观起见，任何两个相邻的球必须涂成不同的颜色。
#找出涂抹球的可能方法的数量。
#
#限制条件
#1≦N≦1000
#2≦K≦1000
#正确答案是最多2^{31}-1。
#
#输入
#输入是由标准输入法提供的，格式如下：
#N K
#
#輸出
#打印画球的可能方法的数量。
#
#输入样本 1
#2 2
#
#输出样本 1
#2
#我们将用0和1来表示颜色。有两种可能的方法：我们可以把左边的球涂成0色，右边的球涂成1色，或者把左边的球涂成1色，右边的球涂成0色。
#
#输入样本 2
#1 10
#
#输出样本 2
#10
#由于只有一个球，我们可以用十种颜色中的任何一种来画它。因此，答案是10。

def 