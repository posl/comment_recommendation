#问题陈述
#你有一个长度为4的数字序列S，你想知道S是以下哪种格式：
#YYMM格式：年的最后两位数和月的两位数（例如：01代表1月），按这个顺序连接起来。
#MMYY格式：月份的两位数和年份的最后两位数，按这个顺序连接起来。
#如果S只在YYMM格式下有效，则打印YYMM；如果S只在MMYY格式下有效，则打印MMYY；如果S在两种格式下都有效，则打印AMBIGUOUS；如果S在两种格式下都无效，则打印NA。
#
#限制条件
#S是一个长度为4的数字序列。
#
#输入
#输入是由标准输入提供的，格式如下：
#S
#
#输出
#打印指定的字符串：YYMM, MMYY, AMBIGUOUS或NA。
#
#输入样本1
#1905
#
#样本输出1
#YYMM
#XX19年5月是一个有效的日期，但19作为一个月是无效的。因此，这个字符串只在YYMM格式下有效。
#
#样本输入2
#0112
#
#样本输出2
#AMBIGUOUS
#十二月XX01和一月XX12都是有效的日期。因此，这个字符串在两种格式下都是有效的。
#
#样本输入3
#1700
#
#样本输出3
#本报告中的0和17都不是有效的月份。
#0和17都不是有效的月份。因此，这个字符串在这两种格式中都是无效的。

def 