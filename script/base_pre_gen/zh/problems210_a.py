#问题陈述
#高桥正在参观一家专门经营卷心菜的商店。
#该店以每头X日元（日本货币）的价格出售卷心菜。
#但是，如果你一次购买超过A头的卷心菜，第(A+1)-头及以后的卷心菜将以每头Y日元出售。
#(保证Y<X。见样本输入/输出
# 1来说明）。
#打印购买N头卷心菜所需的金额。
#
#限制条件
#1 ≦ N ≦ 10^5
#1 ≦ A ≦ 10^5
#1 ≦ y < x ≦ 100
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#N A X Y
#
#輸出
#打印购买N头卷心菜所需的金额（以整数表示）。
#
#输入样本 1
#5 3 20 15
#
#样本输出 1
#90
#你需要为第1至第3颗卷心菜各支付20日元，为第4和第5颗卷心菜各支付15日元。
#因此，你需要为这5颗卷心菜总共支付20+20+20+15+15=90日元。
#
#输入样本 2
#10 10 100 1
#
#样本输出2
#1000

def 