#问题陈述
#我们有一个0到9（包括）之间的N个整数序列：A=(A_1, ..., A_N)，按这个顺序从左到右排列。
#直到序列的长度变成1，我们将重复做下面的操作F或G。
#操作F：删除最左边的两个值（我们称它们为x和y），然后在左端插入（x+y）%10。
#操作G：删除最左边的两个值（我们称它们为x和y），然后在左端插入（x×y）%10。
#这里，a%b表示a除以b时的剩余部分。
#对于每个K=0,1,...,9，请回答以下问题。
#在我们进行操作的2^{N-1}种可能方式中，有多少种方式最终以K为序列的最终值？
#由于答案可能是巨大的，请找出998244353的模数。
#
#限制条件
#2 ≦ N ≦ 10^5
#0 ≦ A_i ≦ 9
#输入的所有数值都是整数。
#
#输入
#输入由标准输入提供，格式如下：
#N
#A_1 ...A_N
#
#输出
#打印10行。
#第i行应包含K=i-1情况的答案。
#
#输入样本 1
#3
#2 7 6
#
#样本输出1
#1
#0
#0
#0
#2
#1
#0
#0
#0
#0
#如果我们先做操作F，后做操作F：序列变成(2,7,6)→(9,6)→(5)。
#如果我们先做操作F，后做操作G：序列变成(2,7,6)→(9,6)→(4)。
#如果我们先做操作G，后做操作F：序列变成(2,7,6)→(4,6)→(0)。
#如果我们先做操作G，后做操作G：序列变成(2,7,6)→(4,6)→(4)。
#
#样本输入2
#5
#0 1 2 3 4
#
#样本输出2
#6
#0
#1
#1
#4
#0
#1
#1
#0
#2

def 