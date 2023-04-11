#问题陈述
#我们有一个正整数a。另外，有一块黑板，上面写着一个以10为底的数字。
#设x是黑板上的数字。高桥可以通过下面的操作来改变这个数字。
#擦去x，写上x乘以a，以10为底数。
#把x看作一个字符串，把最右边的数字移到开头。
#    这个操作只有在x≧10且x不能被10整除时才能进行。
#例如，当a=2，x=123时，高桥可以做以下操作之一。
#擦除x，写下x×a=123×2=246。
#把x看作一个字符串，把123的最右边的数字3移到开头，把数字从123变成312。
#黑板上的数字最初是1。将黑板上的数字改为N所需的最少运算次数是多少？如果没有办法将数字改为N，则打印-1。
#
#限制条件
#2 ≦ a < 10^6
#2 ≦ N < 10^6
#输入的所有数值都是整数。
#
#输入
#输入由标准输入提供，格式如下：
#a N
#
#輸出
#打印答案。
#
#输入样本 1
#3 72
#
#样本输出1
#4
#我们可以用四种操作将黑板上的数字从1变成72，如下所示。
#做第一种类型的操作：1 -> 3.
#做第一种类型的操作：3 -> 9.
#做第一种类型的操作：9 -> 27.
#做第二种类型的操作：27->72。
#在三个或更少的操作中不可能达到72，所以答案是4。
#
#输入样本 2
#2 5
#
#输出样本 2
#-1
#要把黑板上的数字改为5是不可能的。
#
#样本输入3
#2 611
#
#样本输出3
#12
#有一种方法可以将黑板上的数字通过12次运算变成611：1->2->4->8->16->32->64->46->92->29->58->116->611，这是最小的可能。
#
#输入样本 4
#2 767090
#
#样本输出4
#111

def 