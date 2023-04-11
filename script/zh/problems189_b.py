#问题陈述
#高桥有N杯白酒。
#第i杯酒的数量和酒精百分比分别为V_i毫升和P_i%（体积）。
#当高桥的酒精摄入量超过X毫升时就会喝醉。
#他喝醉时喝的是N种白酒中的哪一种？如果他喝了所有的酒也没有醉，则打印-1。
#
#限制条件
#输入的所有数值都是整数。
#1 ≦ N ≦ 10^3
#0 ≦ X ≦ 10^6
#1 ≦ V_i ≦ 10^3
#0 ≦ P_i ≦ 100
#
#输入
#输入由标准输入提供，格式如下：
#N X
#V_1 P_1
#.
#.
#.
#V_N P_N
#
#输出
#如果高桥在喝第i种酒时喝醉了，打印i。如果他在喝完所有的酒后仍未喝醉，则打印-1。
#
#输入示例 1
#2 15
#200 5
#350 3
#
#样品输出1
#2
#第1种酒含有200×(5/(100))=10毫升的酒精。
#第2种酒含有350×（3/（100））=10.5毫升酒精。
#在喝第2种白酒时，他的酒精摄入量首次超过15毫升。
#
#样品输入2
#2 10
#200 5
#350 3
#
#样本输出2
#2
#当他的酒精摄入量正好为X毫升时，他仍然没有醉。
#
#样本输入3
#3 1000000
#1000 100
#1000 100
#1000 100
#
#样本输出3
#-1
#他似乎对酒精有免疫力。

def 