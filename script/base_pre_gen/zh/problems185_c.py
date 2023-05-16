#问题陈述
#有一根长度为L的铁条，呈东西走向。我们将在11个位置切割这根铁条，把它分成12根。在这里，所得到的12根铁条中的每一根都必须有正整数的长度。
#找出进行这种分割的方法的数量。当且仅当这两种方式中只有一种方式有切割的位置时，才认为这两种方式是不同的。
#在这个问题的约束下，可以证明答案是小于2^{63}的。
#
#约束条件
#12 ≦ L ≦ 200
#L是一个整数。
#
#输入
#输入是由标准输入法提供的，格式如下：
#L
#
#輸出
#打印做除法的方法的数量。
#
#输入样本 1
#12
#
#样本输出 1
#1
#只有一个办法：把棒子切成12条，每条长度为1。  
#
#样本输入2
#13
#
#采样输出2
#12
#我们有12个选项：一个是最西边的柱子长度为2，一个是西边第二个柱子长度为2，以此类推。
#
#输入样本3
#17
#
#输出样本3
#4368

def 