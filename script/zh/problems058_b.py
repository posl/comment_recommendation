#问题陈述
#Snuke注册了一个举办编程比赛的新网站。
#他担心自己会忘记密码，于是把密码记了下来。
#由于直接记录密码会给他带来麻烦、
#他做了两本笔记：一本包含奇数位置的字符，另一本包含偶数位置的字符。
#给你两个字符串O和E。O包含奇数位置的字符，保留其相对顺序，E包含偶数位置的字符，保留其相对顺序。
#恢复原来的密码。
#
#限制条件
#O和E由小写英文字母（a - z）组成。
#1 ≦ |O|,|E| ≦ 50
#|O| - |E|为0或1。
#
#输入
#输入是由标准输入法提供的，其格式如下：
#O
#E
#
#输出
#打印原始密码。
#
#输入样本1
#xyz
#abc
#
#样本输出1
#xaybzc
#原始密码是xaybzc。将奇数位置的字符提取出来的结果是xyz，将偶数位置的字符提取出来的结果是abc。
#
#输入样本2
#编码员初学竞赛
#atcoderregularcontest
#
#输出样本2
#编码员的工作职责

def 