#问题陈述
#有一个序列A = (A_0, A_1, ..., A_{N - 1})，有N = 2^{20}项。初始时，每个项都是-1。
#按顺序处理Q个查询。第i个查询（1 ≦ i ≦ Q）由一个整数t_i描述，如t_i = 1或t_i = 2，以及另一个整数x_i，如下。
#如果t_i=1，依次进行以下操作。
#定义一个整数h为h=x_i。
#当A_{h mod N}≠-1时，不断向h加1。我们可以证明，在这个问题的约束条件下，这个过程在有限迭代后结束。
#用x_i替换A_{h mod N}的值。
#如果t_i=2，则打印当时的A_{x_i mod N}的值。
#这里，对于整数a和b，a mod b表示a除以b时的余数。
#
#限制条件
#1 ≦ Q ≦ 2 × 10^5
#t_i在{ 1, 2 }中  (1 ≦ i ≦ Q)
#0 ≦ x_i ≦ 10^{18}。  (1 ≦ i ≦ Q)
#至少有一个i (1 ≦ i ≦ Q)使得t_i = 2。
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#Q
#t_1 x_1
#.
#.
#.
#t_{Q} x_{Q}
#
#输出
#对于每个t_i = 2的查询，用一行打印出响应。保证至少有一个这样的查询。
#
#输入样本 1
#4
#1 1048577
#1 1
#2 2097153
#2 3
#
#样本输出1
#1048577
#-1
#我们有x_1 mod N = 1，所以第一个查询设定A_1 = 1048577。
#在第二个查询中，最初我们有h = x_2，对于它，A_{h mod N} = A_{1} ≠ -1，所以我们在h上加1。≠ 现在我们有A_{h mod N} = A_{2} = -1，所以这个查询设置A_2 = 1。
#在第三个查询中，我们打印出A_{x_3 mod N} = A_{1} = 1048577。
#在第四个查询中，我们打印出A_{x_4 mod N} = A_{3} = -1。
#注意，在这个问题中，N=2^{20}=1048576是一个常数，没有在输入中给出。

def 