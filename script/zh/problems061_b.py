#问题陈述
#有N个城市和M条道路。
#第i条道路（1≤i≤M）双向连接两个城市a_i和b_i（1≤a_i，b_i≤N）。
#连接同一对两个城市的道路可能不止一条。
#对于每个城市，有多少条道路与该城市相连？
#
#约束条件
#2≤N,M≤50
#1≤a_i,b_i≤N
#a_i ≠ b_i
#所有的输入值都是整数。
#
#输入
#输入是由标准输入给出的，格式如下：  
#N M
#a_1 b_1
#:
#a_M b_M
#
#输出
#用N行打印答案。
#在第i行（1≤i≤N），打印连接到城市i的道路数量。
#
#输入样本 1
#4 3
#1 2
#2 3
#1 4
#
#样本输出 1
#2
#2
#1
#1
#城市1与第1条和第3条道路相连。
#城市2与1号和2号公路相连。
#城市3与第2条道路相连。
#城市4连接到第3条道路。
#
#样本输入 2
#2 5
#1 2
#2 1
#1 2
#2 1
#1 2
#
#样本输出2
#5
#5
#
#采样输入3
#8 8
#1 2
#3 4
#1 5
#2 8
#3 7
#5 2
#4 1
#6 8
#
#输出样本3
#3
#3
#2
#2
#2
#1
#1
#2

def 