#问题陈述
#给你一个人的收缩压A和舒张压B。
#找到平均动脉压C，我们定义如下：
#C=（（A-B）/（3））+B。
#
#限制条件
#50 ≦ b ≦ a ≦ 300
#输入的所有数值都是整数。
#
#输入
#输入由标准输入提供，格式如下：
#A B
#
#输出
#打印数值C。
#当你的输出与我们的答案的绝对或相对误差最多为10^{-5}时，你的输出被认为是正确的。
#
#输入样本 1
#130 100
#
#样本输出1
#110
#我们有C=（（130-100）/（3））+100=10+100=110。
#
#样本输入2
#300 50
#
#样本输出2
#133.3333333
#注意，虽然输入的所有数值都是整数，但输出的数值可能不是整数。
#
#输入示例 3
#123 123
#
#输出示例 3
#123

def 