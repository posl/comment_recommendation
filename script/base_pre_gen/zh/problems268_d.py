#问题陈述
#高桥在决定一个服务的用户名时遇到了困难。  请写一段代码来帮助他。
#找到一个满足以下所有条件的字符串X：
#X是通过以下程序得到的：
#让S_1', S_2', ..., S_N'是S_1, S_2, ..., S_N的一个置换。  让X是S_1', (1份或多份_), S_2', (1份或多份_), ..., (1份或多份_), 和S_N'的连接，按这个顺序。
#X的长度在3和16之间，包括在内。
#X不与M个字符串T_1,T_2,...,T_M中的任何一个重合。
#如果没有满足所有条件的X，则打印-1。
#
#限制条件
#1 ≦ N ≦ 8
#0 ≦ M ≦ 10^5
#N和M是整数。
#1 ≦ |S_i| ≦ 16
#N-1+sum{|S_i|} ≦ 16≦ 16
#S_i ≠ S_j，如果i ≠ j。
#S_i是一个由小写英文字母组成的字符串。
#3 ≦ |T_i| ≦ 16
#T_i ≠ T_j 如果 i ≠ j.
#T_i是一个由小写英文字母和_组成的字符串。
#
#输入
#输入是由标准输入法提供的，格式如下：
#N M
#S_1
#S_2
#.
#.
#.
#S_N
#T_1
#T_2
#.
#.
#.
#T_M
#
#输出
#打印一个满足所有条件的字符串X。  如果没有满足所有条件的X，则打印-1。
#如果有多个解决方案，打印其中任何一个。
#
#输入样本 1
#1 1
#chokudai
#chokudai
#
#样本输出 1
#-1
#唯一满足第一和第二个条件的字符串是X= chokudai，但它与T_1重合。
#因此，不存在满足所有条件的X，所以应该打印-1。
#
#输入样本 2
#2 2
#choku
#dai
#chokudai
#choku_dai
#
#样本输出2
#dai_choku
#像choku__dai这样的字符串（在choku和dai之间有两个_）也满足所有的条件。
#
#输入样本 3
#2 2
#chokudai
#atcoder
#chokudai_atcoder
#编码机_初学台
#
#样本输出3
#-1
#chokudai__atcoder和atcoder__chokudai（在chokudai和atcoder之间有两个_）的长度为17，这违反了第二个条件。
#
#输入样本 4
#4 4
#ab
#cd
#ef
#gh
#hoge
#fuga
#____
#_ab_cd_ef_gh_
#
#样本输出4
#ab__ef___cd_gh
#给定的T_i可能包含一个无法通过第一个条件中描述的程序获得的字符串。

def 