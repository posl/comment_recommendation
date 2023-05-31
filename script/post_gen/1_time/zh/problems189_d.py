#问题陈述
#给出N个字符串S_1,...,S_N，其中每个字符串都是AND或OR。
#求N+1个变量(x_0,...,x_N)的数组，其中每个元素都是真或假的，使得下面的计算结果y_N为真：
#y_0=x_0；
#对于i≧1，如果S_i是AND，y_i=y_{i-1} ∧ x_i；如果S_i是OR，y_i=y_{i-1} ∨ x_i。
#这里，a ∧ b 和 a ∨ b 是逻辑运算符。
#
#限制条件
#1 ≦ N ≦ 60
#S_i 是 AND 或 OR。
#
#输入
#输入由标准输入提供，格式如下：
#N
#S_1
#.
#.
#.
#S_N
#
#输出
#打印答案。
#
#输入样本 1
#2
#AND
#OR
#
#样本输出1
#5
#例如，如果(x_0,x_1,x_2)=(True,False,True)，我们有y_2=True，如下所示：
#y_0=x_0=True
#y_1=y_0 ∧ x_1=True ∧ False=False
#y_2=y_1 ∨ x_2 = False ∨ True=True
#所有五个图元 (x_0,x_1,x_2) 的结果是 y_2 = True，如下所示：
#(True,True,True)
#(True,True,False)
#(True,False,True)
#(False,True,True)
#(False,False,True)
#
#样本输入2
#5
#OR
#OR
#OR
#OR
#OR
#
#样本输出2
#63
#所有的图元，除了一个完全填写为 "假 "的图元外，其他图元的结果都是y_5=真。

def 