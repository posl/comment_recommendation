#问题陈述
#给你一个长度为N的序列A=（A_1, A_2, ..., A_N）。
#对于每个K = 0, 1, 2, ..., N-1，解决以下问题。
#找出介于1和N之间的整数i的数目（包括在内），以便：
#A正好包含大于A_i的K个不同的整数。  
#
#
#限制条件
#1 ≦ N ≦ 2 × 10^5
#1 ≦ A_i ≦ 10^9
#输入的所有数值都是整数。
#
#输入
#输入来自标准输入，其格式如下：
#N
#A_1 A_2 ...A_N
#
#输出
#打印N行。
#对于i=1，2，...，N，第i行应该包含K=i-1的答案。
#
#输入样本 1
#6
#2 7 1 8 2 8
#
#样本输出 1
#2
#1
#2
#1
#0
#0
#例如，我们将找到K=2的答案。
#关于A_1=2，A包含两个大于A_1的整数：7和8。
#关于A_2=7，A包含一个大于A_2的整数：8。
#关于A_3=1，A包含3个大于A_3的不同的整数：2，7，和8。
#关于A_4=8，A包含比A_4大的0个不同的整数（不存在这样的整数）。
#关于A_5=2，A包含两个大于A_5的整数：7和8。
#关于A_6=8，A包含0个大于A_6的不同整数（没有这样的整数）。
#因此，有两个i，i=1和i=5，这样A就正好包含了K=2个大于A_i的不同整数。  因此，K=2的答案是2。
#
#输入样本 2
#1
#1
#
#采样输出2
#1
#
#样品输入3
#10
#979861204 57882493 979861204 447672230 644706927 710511029 763027379 710511029 447672230 136397527
#
#样本输出3
#2
#1
#2
#1
#2
#1
#1
#0
#0
#0

def 