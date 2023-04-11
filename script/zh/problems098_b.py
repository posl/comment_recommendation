#问题陈述
#给你一个由小写英文字母组成的长度为N的字符串S。
#我们将在一个位置将这个字符串切成两个字符串X和Y。
#在这里，我们希望最大限度地增加X和Y中包含的不同字母的数量。
#请找出当我们在最佳位置切割字符串时，X和Y中包含的不同字母的最大可能数量。
#
#限制条件
#2 ≦ N ≦ 100
#|S| = N
#S由小写英文字母组成。
#
#输入
#输入由标准输入法提供，格式如下：
#N
#S
#
#輸出
#打印X和Y中包含的最大可能的不同字母数。
#
#输入样本1
#6
#aabbca
#
#样本输出1
#2
#如果我们把第三和第四个字母之间的字符串切成X = aab和Y = bca，那么X和Y中包含的字母都是a和b。
#在X和Y中永远不会有三个或更多不同的字母，所以答案是2。
#
#输入样本2
#10
#aaaaaaaaaa
#
#样本输出2
#1
#无论我们如何划分S，只有a会同时包含在X和Y中。
#
#输入样本3
#45
#tgxgdqkyjzhyputjjtllptdfxocrylqfqjynmfbfucbir
#
#样本输出3
#9

def 