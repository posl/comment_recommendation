#问题陈述
#我们有9K张卡片。对于每个i=1，2，...，9，都有K张写有i的牌。
#我们随机洗了这些牌，并向高桥和青木各发了五张牌--四张正面朝上，一张正面朝下。
#给你一个字符串S，代表发给高桥的牌，一个字符串T，代表发给青木的牌。
#S和T是各有五个字符的字符串。每个字符串的前四个字符都是1，2，...，或9，代表写在正面朝上的牌上的数字。每个字符串的最后一个字符是#，代表牌面朝下。
#我们把五张牌的得分定义为sum_{i=1}^9 i × 10^{c_i}，其中c_i是写有i的牌的数量。
#当高桥的牌分高于青木的牌分时，高桥获胜。
#求高桥获胜的概率。
#
#限制条件
#2 ≤ K ≤ 10^5
#|S| = |T| = 5
#S和T的第一个到第四个字符都是1，2，...，或9。
#每个数字1，2，...，和9在S和T中总共最多出现K次。
#S和T中每一个的第五个字符是#。
#
#输入
#输入是由标准输入法提供的，其格式如下：
#K
#S
#T
#
#输出
#打印高桥获胜的概率，以小数表示。
#当你的答案与我们的答案的绝对或相对误差不超过10^{-5}时，将被判定为正确。
#
#输入样本 1
#2
#1144#
#2233#
#
#样本输出1
#0.4444444444444444
#例如，如果高桥的手牌是11449，青木的手牌是22338，高桥的分数是100+2+3+400+5+6+7+8+90=621，青木的分数是1+200+300+4+5+6+7+80+9=612，结果是高桥赢。
#当高桥的面朝下的牌上的数字大于青木的面朝下的牌上的数字时，高桥就赢了，所以高桥将以frac49的概率获胜。
#
#输入样本2
#2
#9988#
#1122#
#
#样本输出2
#1.0
#
#样本输入3
#6
#1122#
#2228#
#
#样本输出3
#0.001932367149758454
#只有当高桥的手牌是11222，而青木的手牌是22281时，高桥才会赢，概率是（2/1035）。
#
#样本输入4
#100000
#3226#
#3597#
#
#样本输出4
#0.6296297942426154

def 