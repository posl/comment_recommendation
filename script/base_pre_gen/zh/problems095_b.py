#问题陈述
#Akaki是一名糕点师，只用一种叫做 "Okashi no Moto"（字面意思是 "糕点材料"，下面简称为Moto）的粉末作为原料，就可以制作N种甜甜圈。这些甜甜圈被称为甜甜圈1，甜甜圈2，...，甜甜圈N。为了制作一个甜甜圈i（1≤i≤N），她需要消耗m_i克的摩托。她不能制作非整数的甜甜圈，如0.5个甜甜圈。
#现在，她有X克的Moto。她决定为今晚的聚会制作尽可能多的甜甜圈。然而，由于客人的口味不同，她将遵守以下条件：
#对于N种甜甜圈中的每一种，至少要做一个该种甜甜圈。
#这里最多可以做多少个甜甜圈？她不一定要把她的Moto全部吃完。另外，在这个问题的约束下，总是有可能遵守这个条件的。
#
#约束条件
#2 ≤ N ≤ 100
#1 ≤ m_i ≤ 1000
#m_1 + m_2 + ...+ m_N ≤ X ≤ 10^5
#输入的所有数值都是整数。
#
#输入
#输入由标准输入提供，其格式如下：
#N X
#m_1
#m_2
#:
#m_N
#
#输出
#打印在该条件下可制作的最大甜甜圈数量。
#
#样本输入1
#3 1000
#120
#100
#140
#
#样本输出1
#9
#她有1000克摩托，可以做三种甜甜圈。如果她为这三种甜甜圈各做一个，她就会消耗120+100+140=360克的摩托。从剩下的640克摩托中，她可以再做六个甜甜圈2。这样，她总共可以做9个甜甜圈，这是最大值。
#
#输入样本2
#4 360
#90
#90
#90
#90
#
#样本输出2
#4
#为这四种人各做一个甜甜圈，消耗了她所有的摩托。
#
#样本输入3
#5 3000
#150
#130
#150
#130
#110
#
#样本输出3
#26

def 