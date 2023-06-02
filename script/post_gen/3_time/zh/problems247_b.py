#问题陈述
#有N个人，编号为Person 1, Person 2, ..., and Person N. Person i有一个姓氏s_i和一个名字t_i。
#考虑给这N个人中的每个人起一个绰号。  第i人的绰号a_i应该满足以下所有条件。
#a_i与i人的姓氏或名字重合。  换言之，a_i = s_i和/或a_i = t_i成立。
#a_i不与任何其他人的姓氏和名字重合。  换句话说，对于所有整数j，如1≦j≦N且i≠j，则a_i≠s_j和a_i≠t_j成立。
#有没有可能给所有的N个人起绰号？  如果有可能，打印Yes；否则，打印No。
#
#限制条件
#2 ≦ N ≦ 100
#N是一个整数。
#s_i和t_i是长度在1到10之间（包括10）的字符串，由小写英文字母组成。
#
#输入
#输入是由标准输入法提供的，其格式如下：
#N
#s_1 t_1
#s_2 t_2
#.
#.
#.
#s_N t_N
#
#输出
#如果有可能给所有N个人起绰号，打印Yes；否则，打印No。
#
#输入样本 1
#3
#tanaka taro
#tanaka jiro
#suzuki hanako
#
#样本输出1
#Yes
#下面的分配符合问题陈述中描述的昵称条件：a_1 = taro，a_2 = jiro，a_3 = hanako。  (a_3也可以是suzuki)。
#然而，请注意，我们不能让a_1=tanaka，这违反了昵称的第二个条件，因为第2个人的姓氏s_2也是tanaka。
#
#样本输入2
#3
#aaa bbb
#xxx aaa
#bbb yyy
#
#样本输出2
#No
#没有办法给出满足问题陈述中条件的昵称。
#
#输入样本3
#2
#tanaka taro
#tanaka taro
#
#样本输出3
#No
#可能有一对具有相同姓氏和相同名字的人。
#
#样本输入4
#3
#takahashi chokudai
#aoki kensho
#snu ke
#
#样本输出4
#Yes
#我们可以让a_1 = chokudai, a_2 = kensho, and a_3 = ke。

def 