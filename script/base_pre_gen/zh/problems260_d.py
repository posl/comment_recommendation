#问题陈述
#有一副牌，由N张面朝下的牌组成，上面写着从1到N的整数。  从上面第i张牌上的整数是P_i。
#利用这副牌，你将进行N次行动，每次行动包括以下步骤：
#从这副牌中抽出最上面的一张牌。  让X成为写在上面的整数。
#将抽出的牌面朝上叠放在桌面上最上面的牌中整数最小的那张牌上，上面写着大于或等于X的整数。  如果桌子上没有这样的牌，就把抽到的牌正面朝上放在桌子上，不堆在任何牌上。
#然后，如果桌子上有一堆由K张面朝上的牌组成的牌，就把这些牌全部吃掉。  被吃掉的牌都会从桌子上消失。
#对于每张牌，找出N次行动中哪一次吃了它。  如果这张牌直到最后才被吃掉，请报告这一事实。
#
#限制条件
#输入的所有数值都是整数。
#1 ≦ k ≦ n ≦ 2 × 10^5
#P是(1,2,...,N)的排列组合（即通过重新排列(1,2,...,N)得到的序列）。
#
#输入
#输入是由标准输入给出的，格式如下：
#N K
#P_1 P_2 ...P_N
#
#输出
#打印N行。
#第i行（1 ≦ i ≦ N）应该描述写有整数i的卡片。  具体来说、
#如果写有i的牌在第x步中被吃掉，打印x；
#如果这张牌在任何一步中都没有被吃掉，则打印-1。
#
#输入样本 1
#5 2
#3 5 2 1 4
#
#样本输出1
#4
#3
#3
#-1
#4
#在这个输入中，P=（3，5，2，1，4），K=2。
#在第1步棋中，写有3的牌被放在桌子上，正面朝上，没有叠在任何牌上。
#在第2步棋中，写有5的牌正面朝上放在桌子上，不叠加在任何牌上。
#在第3步棋中，写有2的牌正面朝上叠放在写有3的牌上。
#现在有一堆K=2的牌面朝上，上面写着2和3，所以这些牌被吃掉了。
#在第4步中，写有1的牌被正面朝上叠放在写有5的牌上。
#现在有一堆K=2的牌面朝上，上面写着1和5，所以这些牌被吃掉了。
#在第5步中，写有4的牌被放在桌子上，正面朝上，没有叠在任何牌上。
#写有4的牌直到最后才被吃掉。
#
#输入样本 2
#5 1
#1 2 3 4 5
#
#样本输出2
#1
#2
#3
#4
#5
#如果K=1，每张牌在放上桌后都会在一招之内立即被吃掉。
#
#输入样本 3
#15 3
#3 14 15 9 2 6 5 13 1 7 10 11 8 12 4
#
#样本输出 3
#9
#9
#9
#15
#15
#6
#-1
#-1
#6
#-1
#-1
#-1
#-1
#6
#15

def 