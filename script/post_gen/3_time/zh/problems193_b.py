#问题陈述
#高桥想购买流行的视频游戏机，名为Play Snuke。
#有N家商店出售Play Snuke：商店1，2，...，N。商店i离高桥现在所在的地方有A_i分钟的步行路程，以P_i日元（日本货币）出售Play Snuke，目前有X_i Play Snuk的库存。
#现在，高桥会步行到其中一家商店，如果他到那里时仍有库存，就会购买Play Snuke。
#然而，Play Snuke是如此受欢迎，以至于每家商店的游戏机库存数量（如果有的话）将在以下时刻减少1：0.5，1.5，2.5，...分钟后。
#判断高桥是否可以购买Play Snuke。如果他能，求出购买的最低资金量。
#
#限制条件
#输入的所有数值都是整数。
#1 ≤ N ≤ 10^5
#1 ≤ A_i, P_i, X_i ≤ 10^9
#
#输入
#输入由标准输入提供，格式如下：
#N
#A_1 P_1 X_1
#.
#.
#.
#A_N P_N X_N
#
#输出
#如果高桥能买到Play Snuke，则打印出买一个Play Snuke所需的最小金额，为整数。
#如果他不能买，打印-1。
#
#输入样本 1
#3
#3 9 5
#4 8 5
#5 7 5
#
#样本输出1
#8
#如果他去1号店，当他到达那里时，那里仍然有2个Play Snukes，他可以用9日元买一个。
#如果他去2号店，当他到达那里时，那里仍然有1个Play Snuke，他可以用8日元买一个。
#如果他去3号店，当他到达那里时，Play Snuke将没有库存；他不能买一个。
#
#输入样本 2
#3
#5 9 5
#6 8 5
#7 7 5
#
#样本输出2
#-1
#
#样本输入3
#10
#158260522 877914575 602436426
#24979445 861648772 623690081
#433933447 476190629 262703497
#211047202 971407775 628894325
#731963982 822804784 450968417
#430302156 982631932 161735902
#880895728 923078537 707723857
#189330739 910286918 802329211
#404539679 303238506 317063340
#492686568 773361868 125660016
#
#样本输出3
#861648772

def 