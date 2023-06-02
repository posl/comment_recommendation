#问题陈述
#求一种产品的税前价格，以便当消费税率为8%和10%时，对其征收的消费税金额分别为A日元和B日元。(日元是日本的货币）。
#这里，税前价格必须是一个正整数，消费税的金额被四舍五入到最近的整数。
#如果有多个价格满足条件，则打印最低的这个价格；如果没有价格满足条件，则打印-1。
#
#限制条件
#1 ≦ A ≦ B ≦ 100
#A和B是整数。
#
#输入
#输入是由标准输入法提供的，其格式如下：
#A B
#
#輸出
#如果有一个满足条件的价格，打印一个代表最低价格的整数；否则，打印-1。
#
#输入样本 1
#2 2
#
#输出示例 1
#25
#如果某种产品的税前价格为25日元，对其征收的消费税金额为：
#当消费税率为8%时：⌊ 25 × 0.08 ⌋ = ⌊ 2 ⌋ = 2日元。
#当消费税率为10%时：⌊ 25 × 0.1 ⌋ = ⌊ 2.5 ⌋ = 2日元。
#因此，25日元的价格就满足了条件。还有其他可能的价格，如26日元，但打印出最小的这种价格，即25。
#
#输入样本 2
#8 10
#
#样本输出 2
#100
#如果一种产品的税前价格为100日元，对其征收的消费税金额为：
#当消费税率为8%时： ⌊ 100 × 0.08 ⌋ = 8日元。
#当消费税率为10%时： ⌊ 100 × 0.1 ⌋ = 10日元。
#
#样本输入3
#19 99
#
#样本输出3
#-1
#没有满足这个条件的税前价格，所以打印-1。

def 