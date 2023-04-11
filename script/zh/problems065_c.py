#问题陈述
#Snuke有N只狗和M只猴子。他想让它们排成一排。
#正如一句日本谚语所说，这些狗和猴子的关系不好。("ken'en no naka"，字面意思是 "狗和猴子的关系"，意思是相互憎恨的关系。)斯努克试图通过安排这些动物，使它们既没有相邻的两只狗，也没有相邻的两只猴子，来使它们和解。
#有多少个这样的安排？找出10^9+7的模数（因为动物无法理解比这更大的数字）。
#这里，狗和猴子都是可以区分的。另外，两个相互颠倒的排列也是可以区分的。
#
#约束条件
#1 ≤ N,M ≤ 10^5
#
#输入
#输入由标准输入提供，格式如下：
#N M
#
#输出
#打印可能的安排的数量，模数为10^9+7。
#
#输入样本 1
#2 2
#
#输出样本 1
#8
#我们将用A和B表示狗，用C和D表示猴子：ACBD, ADBC, BCAD, BDAC, CADB, CBDA, DACB 和 DBCA。
#
#输入样本 2
#3 2
#
#样本输出2
#12
#
#样本输入3
#1 8
#
#采样输出3
#0
#
#采样输入4
#100000 100000
#
#样本输出4
#530123477

def 