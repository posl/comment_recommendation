#问题陈述
#在AtCoder市，有五根天线站成一条直线。它们从西到东被称为天线A、B、C、D和E，它们的坐标分别是A、B、C、D和E。
#如果两个天线之间的距离为k或更小，它们可以直接通信，如果距离大于k，它们就不能通信。
#确定是否存在一对不能直接通信的天线。
#在此，假设在坐标p和q（p<q）的两根天线之间的距离是q-p。
#
#约束条件
#a、b、c、d、e和k是0到123（包括）之间的整数。
#a < b < c < d < e
#
#输入
#输入由标准输入提供，格式如下：
#a
#b
#c
#d
#e
#k
#
#输出
#如果存在一对不能直接通信的天线，则打印:(；如果不存在这样的一对天线，则打印Yay!
#
#输入示例 1
#1
#2
#4
#8
#9
#15
#
#输出样本1
#耶!
#在这种情况下，没有一对天线不能直接通信，因为：
#A和B之间的距离是2-1=1
#A和C之间的距离是4-1=3
#A和D之间的距离是8-1=7
#A和E之间的距离是9-1=8
#B和C之间的距离是4-2=2
#B和D之间的距离是8-2=6
#B和E之间的距离是9-2=7
#C和D之间的距离是8-4=4
#C和E之间的距离是9-4=5
#D和E之间的距离是9-8=1
#并且没有一个大于15。因此，正确的输出是Yay！。
#
#输入样本2
#15
#18
#26
#35
#36
#18
#
#样本输出2
#:(
#在这种情况下，天线A和D之间的距离是35-15=20，超过了18，所以它们不能直接通信。
#因此，正确的输出是：（。

def 