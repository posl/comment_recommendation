#问题陈述
#Katsusando喜欢煎蛋饭。
#此外，他还喜欢奶油布丁、里脊牛排等，并认为这些食物都是人人喜爱的。
#为了证明这个假设，他对M种食物进行了调查，问了N个人是否喜欢这些食物。
#第i个人回答说他/她只喜欢A_{i1}-th，A_{i2}-th，...，A_{iK_i}-th的食物。
#求所有N个人喜欢的食物的数量。
#
#限制条件
#输入的所有数值都是整数。
#1 ≦ N, M ≦ 30
#1 ≦ K_i ≦ M
#1 ≦ A_{ij} ≦ M
#对于每个i（1 ≦ i ≦ N），A_{i1}, A_{i2}, ..., A_{iK_i}是不同的。
#
#约束条件
#输入是由标准输入提供的，格式如下：
#N M
#K_1 A_{11}A_{12}...A_{1K_1}
#K_2 A_{21}A_{22} ...A_{2K_2}
#:
#K_N A_{N1}A_{N2} ...A_{NK_N}
#
#输出
#打印所有N个人喜欢的食物的数量。
#
#输入样本 1
#3 4
#2 1 3
#3 1 2 3
#2 3 2
#
#样本输出1
#1
#因为只有第三种食物是三个人都喜欢的，所以应该打印1。
#
#输入样本2
#5 5
#4 2 3 4 5
#4 1 3 4 5
#4 1 2 4 5
#4 1 2 3 5
#4 1 2 3 4
#
#样本输出2
#0
#胜山多的假设被证明是错误的。
#
#样本输入3
#1 30
#3 5 10 30
#
#样本输出 3
#3

def 