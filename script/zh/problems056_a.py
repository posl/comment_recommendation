#问题陈述
#两只鹿，AtCoDeer和TopCoDeer，正在玩一个叫 "诚实或不诚实 "的游戏。
#在这个游戏中，诚实的玩家总是说真话，而不诚实的玩家总是说假话。
#你会得到两个字符a和b作为输入。它们中的每一个都是H或D，并带有以下信息：
#如果a=H，AtCoDeer是诚实的；如果a=D，AtCoDeer是不诚实的。
#如果b=H，AtCoDeer是说TopCoDeer是诚实的；如果b=D，AtCoDeer是说TopCoDeer是不诚实的。
#根据这些信息，判断TopCoDeer是否诚实。
#
#限制条件
#a=H或a=D。
#b=H或b=D。
#
#输入
#输入来自标准输入，其格式如下：
#a b
#
#输出
#如果TopCoDeer是诚实的，打印H；如果他是不诚实的，打印D。
#
#输入样本1
#H H
#
#样本输出1
#H
#在这个输入中，AtCoDeer是诚实的。因此，正如他所说，TopCoDeer是诚实的。
#
#样本输入2
#D H
#
#样本输出2
#D
#在这个输入中，AtCoDeer是不诚实的。因此，与他所说的相反，TopCoDeer是不诚实的。
#
#样本输入3
#D D
#
#样本输出3
#H

def 