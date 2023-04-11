#问题陈述
#阿卡里有n种花，每种都有。
#她要从这些花中选择一种或几种来做花束。
#但是，她讨厌两个数字a和b，所以花束中的花的数量不能是a或b。
#阿卡丽可以做多少种不同的花束？
#找出模数（10^9+7）。
#在这里，如果有一种花在其中一束花中使用，而在另一束花中不使用，则认为两束花是不同的。
#
#限制条件
#输入的所有数值都是整数。
#2 ≦ n ≦ 10^9
#1 ≦ a < b ≦ min(n, 2 × 10^5)
#
#输入
#输入是由标准输入提供的，格式如下：
#n a b
#
#輸出
#打印Akari能做的花束数量，模数为(10^9 + 7)。(如果没有这样的花束，打印0。）
#
#输入样本 1
#4 1 3
#
#输出样本 1
#7
#在这个例子中，Akari可以选择2或4朵花来制作花束。
#有6种方法可以从4种花中选择2种，有1种方法可以选择4种，所以明莉一共可以做7种不同的花束。
#
#输入样本2
#1000000000 141421 173205
#
#样本输出2
#34076506
#打印计数的模数（10^9+7）。

def 