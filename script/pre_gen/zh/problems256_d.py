#问题陈述
#对于实数L和R，让我们用[L,R]表示大于或等于L且小于R的实数的集合。
#给你N个右半开区间[L_i,R_i]。  让S成为它们的集合。  将S表示为最小数量的右半开区间的集合。
#
#限制条件
#1 ≦ N ≦ 2× 10^5
#1 ≦ L_i < R_i ≦ 2× 10^5
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#N
#L_1 R_1
#.
#.
#.
#L_N R_N
#
#输出
#设k是将S表示为其联合体所需的最小数量的右半开区间。   打印包含这k个右半开区间[X_i,Y_i]的k行，按X_i的升序排列，如下：
#X_1 Y_1
#.
#.
#.
#X_k Y_k
#
#样本输入1
#3
#10 20
#20 30
#40 50
#
#样本输出1
#10 30
#40 50
#三个右半开区间[10,20),[20,30),[40,50]的结合等于两个右半开区间[10,30),[40,50]的集合。
#
#样本输入2
#3
#10 40
#30 60
#20 50
#
#样本输出2
#10 60
#三个右半开区间[10,40),[30,60),[20,50]的联合等于一个右半开区间[10,60]的集合。

def 