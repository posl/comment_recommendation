#问题陈述
#有N+1个城镇。第i个城镇正被A_i个怪物攻击。
#我们有N个英雄。第i个英雄可以打败攻击第i个或（i+1）个城镇的怪物，总共最多可以打败B_i个怪物。
#英雄们合作最多可以打败多少个怪物？
#
#限制条件
#输入的所有数值都是整数。
#1 ≦ N ≦ 10^5
#1 ≦ A_i ≦ 10^9
#1 ≦ B_i ≦ 10^9
#
#输入
#输入是由标准输入法提供的，格式如下：
#N
#A_1 A_2 ...A_{N+1}
#B_1 B_2 ...B_N
#
#输出
#打印英雄们能打败的最大怪物总数。
#
#输入样本 1
#2
#3 5 2
#4 5
#
#样本输出1
#9
#如果英雄们按以下方式选择要击败的怪物，他们总共可以击败9个怪物，这是最大的结果。
#第一位英雄击败了攻击第一个城镇的两个怪物和攻击第二个城镇的两个怪物。
#第二位英雄击败了攻击第二座城镇的三只怪物和攻击第三座城镇的两只怪物。
#
#输入样本2
#3
#5 6 3 8
#5 100 8
#
#样本输出2
#22
#
#样本输入3
#2
#100 1 1
#1 100
#
#样本输出 3
#3

def 