#问题陈述
#黑板上写有三个正整数A、B和C。E869120进行了以下操作K次：
#选择一个写在黑板上的整数，让所选择的整数为n。
#经过K次运算后，写在黑板上的整数的最大可能之和是多少？
#
#限制条件
#A，B和C是1到50之间的整数（包括在内）。
#K是1到10（包括10）之间的整数。
#
#输入
#输入由标准输入提供，格式如下：
#A B C
#K
#
#輸出
#打印写在黑板上的整数的最大可能之和，经过E869220的K次运算。
#
#输入样本 1
#5 3 11
#1
#
#样本输出1
#30
#在这个例子中，5、3、11最初被写在黑板上，E869120可以执行一次操作。
#有三个选择：  
#双倍5：操作后写在黑板上的整数是10，3，11。
#双3：操作后写在黑板上的整数是5，6，11。
#双11：操作后写在黑板上的整数是5，3，22。
#如果他选择3，那么之后写在黑板上的整数之和是5+3+22=30，是1到3中最大的一个。  
#
#输入样本 2
#3 3 4
#2
#
#样本输出2
#22
#E869120可以进行两次操作。最终写在黑板上的整数之和被最大化，如下所示：  
#首先，将4加倍。现在写在黑板上的整数是3，3，8。
#接下来，将8翻倍。现在写在黑板上的整数是3，3，16。  
#那么，最终写在黑板上的整数之和是3+3+16=22。

def 