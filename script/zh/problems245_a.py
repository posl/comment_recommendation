#问题陈述
#有一天，高桥在A点过B分准时起床（24小时制），而青木在C点过D分1秒准时起床。
#如果高桥比青木起得早，就打印高桥；否则就打印青木。
#
#限制条件
#0 ≦ A ≦ 23
#0 ≦ B ≦ 59
#0 ≦ C ≦ 23
#0 ≦ D ≦ 59
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#A B C D
#
#輸出
#如果高桥比青木起得早，打印高桥；否则，打印青木。
#
#输入样本 1
#7 0 6 30
#
#输出样本1
#青木
#高桥在7点整起床，而青木在6点30分1秒时起床。
#Aoki是第一个起床的，所以Aoki应该被打印出来。
#
#输入样本2
#7 30 7 30
#
#样本输出2
#高桥
#高桥在7点半准时起床，而青木在7点30分1秒时起床。
#只差一秒，高桥是第一个起床的，所以高桥应该被打印出来。
#
#样本输入3
#0 0 23 59
#
#样本输出3
#高桥
#一天中的0:00是0:01之前的一分钟，而不是23:59之后的一分钟（"24:00"）。
#因此，高桥是第一个起床的，所以高桥应该被打印出来。

def 