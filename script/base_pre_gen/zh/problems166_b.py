#问题陈述
#一个镇上住着N个叫Snuke 1, Snuke 2, ..., Snuke N的人。
#这个镇上有K种零食出售，称为零食1，零食2，...，零食K：Snuke A_{i, 1}, A_{i, 2}, ..., A_{i, {d_i}}。
#高桥将在这个小镇上走来走去，对没有零食的Snukes进行恶作剧。有多少个Snukes会成为高桥的恶作剧的受害者？
#
#限制条件
#输入的所有数值都是整数。
#1 ≦ N ≦ 100
#1 ≦ K ≦ 100
#1 ≦ d_i ≦ N
#1 ≦ A_{i, 1} < ...< A_{i, d_i} ≦ N
#
#输入
#输入是由标准输入给出的，格式如下：
#N K
#d_1
#A_{1, 1} ...A_{1, d_1}
#.
#.
#.
#d_K
#A_{K, 1} ...A_{K, d_K}
#
#输出
#打印答案。
#
#输入样本 1
#3 2
#2
#1 3
#1
#3
#
#样本输出1
#1
#Snuke 1有零食1。
#Snuke 2没有零食。
#Snuke 3有Snack 1和2。
#因此，将有一个受害者：Snuke 2。
#
#输入样本 2
#3 3
#1
#3
#1
#3
#1
#3
#
#样本输出2
#2

def 