#问题陈述
#高桥王国使用的硬币有1日元硬币、2日元硬币、......和10日元硬币。这里，N！=1×2×...。× N.
#高桥有100个各种类型的硬币，他要买一个价值P日元的产品，给出准确的金额，不收零钱。
#我们可以证明，总是有这样的付款方式。
#他在付款时至少需要用多少个硬币？
#
#约束条件
#1 ≦ P ≦ 10^7
#P是一个整数。
#
#输入
#输入由标准输入提供，格式如下：
#P
#
#輸出
#打印所需的最小硬币数。
#
#输入样本1
#9
#
#样本输出1
#3
#通过提供一个(1!=)1日元的硬币，一个(2!=)2日元的硬币，一个(3!=)6日元的硬币，我们可以准确支付价值9日元的产品。没有办法用更少的硬币来支付这个金额。
#
#输入样本2
#119
#
#样本输出2
#10
#我们应该使用一个1日元的硬币，两个2日元的硬币，三个3日元的硬币，四个4日元的硬币。
#
#输入样本3
#10000000
#
#样本输出3
#24

def 