#问题陈述
#给你一个由A、B、C组成的字符串S。
#让S^{(0)}:=S。对于i=1,2,3,...，让S^{(i)}是同时替换S^{(i-1)}中的字符的结果，如下所示：a → bc，b → ca，c → ab。
#回答Q查询。第i个查询如下。
#从S^{(t_i)}的开头打印出第k_i个字符。
#
#约束条件
#S是一个长度在1到10^5（包括）之间的字符串，由A、B、C组成。
#1 ≦ Q ≦ 10^5
#0 ≦ t_i ≦ 10^{18}。
#1 ≦ k_i ≦ min(10^{18}, the length of S^{(t_i)})
#Q, t_i, k_i是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#S
#Q
#t_1 k_1
#t_2 k_2
#.
#.
#.
#t_Q k_Q
#
#输出
#按照索引的升序处理Q个查询，也就是按照给定的顺序。每个答案后面都应该有一个换行。
#
#输入样本1
#ABC
#4
#0 1
#1 1
#1 3
#1 6
#
#样本输出1
#A
#B
#C
#B
#我们有S^{(0)}=ABC，S^{(1)}=BCCAAB。
#因此，查询的答案按照给定的顺序是A、B、C、B。
#
#输入样本2
#CBBAACCCCC
#5
#57530144230160008 659279164847814847
#29622990657296329 861239705300265164
#509705228051901259 994708708957785197
#176678501072691541 655134104344481648
#827291290937314275 407121144297426665
#
#样本输出2
#A
#A
#C
#A
#A

def 