#问题陈述
#当且仅当以下所有条件得到满足时，一个奇数长度的字符串S被称为是一个强宫格：
#S是一个调色板。
#由S的第1至((N-1)/2)个字符组成的字符串是一个回文。
#由S的(N+3)/2-st到N-th字符组成的字符串是一个宫格。
#判断S是否是一个强回文。
#
#约束条件
#S由小写英文字母组成。
#S的长度是3到99（包括）之间的奇数。
#
#输入
#输入是由标准输入法提供的，其格式如下：
#S
#
#输出
#如果S是一个强回文，打印Yes；
#否则，打印No。
#
#输入样本1
#Akasaka
#
#样本输出1
#是
#S是akasaka。
#由第1至第3个字符组成的字符串是akasaka。
#由第5个到第7个字符组成的字符串是阿卡。
#所有这些都是回文，所以S是一个强回文。
#
#输入样本2
#水平
#
#样本输出2
#没有
#
#采样输入3
#atcoder
#
#样品输出3
#没有

def 