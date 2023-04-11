#问题陈述
#我们有一个长度为N的序列，由非负整数组成。考虑对这个序列进行以下操作，直到这个序列中的最大元素变成N-1或更小。
#确定序列中最大的元素（如果有多个，选择一个）。将这个元素的值减少N，并将其他元素各增加1。
#可以证明，经过有限次数的运算，序列中的最大元素会变成N-1或更小。
#给你一个整数K，找出一个整数序列a_i，使我们执行上述操作的次数恰好是K，可以证明在这个问题的输入和输出约束下，总是有这样一个序列。
#
#约束条件
#0 ≤ K ≤ 50 × 10^{16}
#
#输入
#输入由标准输入提供，格式如下：
#K
#
#输出
#以下列格式打印一个解决方案：
#N
#a_1 a_2 ... a_N
#这里，2≤N≤50和0≤a_i≤10^{16}的情况下，2≤N≤50。+ 1000必须成立。
#
#样本输入1
#0
#
#采样输出1
#4
#3 3 3 3
#
#样本输入2
#1
#
#样品输出2
#3
#1 0 3
#
#样本输入3
#2
#
#采样输出3
#2
#2 2
#该操作将被执行两次：[2, 2] -> [0, 3] -> [1, 1]。
#
#输入样本 4
#3
#
#样本输出4
#7
#27 0 0 0 0 0 0
#
#样本输入5
#1234567894848
#
#样本输出5
#10
#1000 193 256 777 0 1 1192 1234567891011 48 425

def 