#问题陈述
#一共有A+B只猫和狗。
#其中，已知A是猫，但其余的B既不是猫也不是狗。
#请判断在这些A+B的动物中是否有可能正好有X只猫。
#
#限制条件
#1 ≦ A ≦ 100
#1 ≦ B ≦ 100
#1 ≦ X ≦ 200
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#A B X
#
#輸出
#如果有可能正好有X只猫，打印YES；如果不可能，打印NO。
#
#输入样本 1
#3 5 4
#
#输出示例 1
#是
#如果在B=5只动物中，有一只猫和四只狗，那么总共有X=4只猫。
#
#样本输入2
#2 2 6
#
#样本输出2
#NO
#即使所有的B=2的动物都是猫，但总共也不到X=6只猫。
#
#样本输入3
#5 3 2
#
#样本输出 3
#NO
#即使B=3的动物都是狗，但总共也有超过X=2的猫。

def 