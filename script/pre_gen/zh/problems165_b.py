#问题陈述
#高桥在AtCoder银行有一笔100日元（日本的货币）的存款。
#该银行的年利率为1%，每年复利。(小于1日元的部分被舍弃）。
#假设除利息外没有其他因素影响高桥的余额，那么在多少年后，余额首次达到X日元或以上？
#
#限制条件
# 101 ≦ X ≦ 10^{18}
#输入的所有数值都是整数。
#
#输入
#输入由标准输入提供，其格式如下：
#X
#
#輸出
#打印高桥的余额首次达到X日元或以上所需的年数。
#
#样本输入1
#103
#
#样本输出1
#3
#一年后的余额为101日元。
#两年后的余额是102日元。
#三年后的余额是103日元。
#因此，余额需要三年才能达到103日元或以上。
#
#样本输入2
#1000000000000000000
#
#样本输出2
#3760
#
#样本输入3
#1333333333
#
#样本输出3
#1706

def 