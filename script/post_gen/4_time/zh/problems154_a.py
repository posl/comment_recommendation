#问题陈述
#我们有A个球，每个球上都写着字符串S，B个球上写着字符串T。
#高桥从这些球中选择了一个写有U的球并把它扔掉。
#求现在有多少个写有字符串S的球和写有字符串T的球？
#
#限制条件
#S、T和U是由小写英文字母组成的字符串。
#S和T的长度都在1到10之间（包括10）。
#S不=T
#S=U或T=U。
#1 ≦ A,B ≦ 10
#A和B是整数。
#
#输入
#输入由标准输入法提供，格式如下：
#S T
#A B
#U
#
#输出
#打印答案，中间有空格。
#
#输入样本1
#红色 蓝色
#3 4
#红色
#
#样本输出1
#2 4
#高桥选择了一个写有红色的球，然后把它扔掉。
#现在我们有两个写着S字符串的球和四个写着T字符串的球。
#
#样本输入2
#红色 蓝色
#5 5
#蓝色
#
#样本输出2
#5 4
#高桥选择了一个写有蓝色的球，然后把它扔掉。
#现在我们有五个写着S字符串的球和四个写着T字符串的球。

def 