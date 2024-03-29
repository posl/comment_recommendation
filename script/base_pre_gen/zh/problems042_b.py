#问题陈述
#Iroha有一串N个字符串S_1, S_2, ..., S_N。每个字符串的长度是L。
#她将所有的字符串按一定的顺序连接起来，以产生一个长字符串。
#在她能以这种方式产生的所有字符串中，找出词典上最小的一个。
#这里，一个字符串s=s_1s_2s_3...s_n在词典上比另一个字符串t=t_1t_2t_3...t_m小，当且仅当下列情况之一成立：
#存在一个索引i(1≦i≦min(n,m))，使得s_j = t_j对于所有的索引j(1≦j<i)，并且s_i<t_i。
#对于所有整数i(1≦i≦min(n,m))，且n<m，s_i = t_i。
#
#约束条件
#1 ≦ N, L ≦ 100
#对于每一个i，S_i的长度等于L。
#对于每个i，S_i都由小写字母组成。
#
#输入
#输入是由标准输入给出的，格式如下：
#N L
#S_1
#S_2
#:
#S_N
#
#输出
#打印Iroha能产生的最小的词汇表。
#
#输入样本 1
#3 3
#dxx
#axx
#cxx
#
#输出样本1
#axxcxxdxx
#应使用以下顺序：Axx, cxx, dxx。

def 