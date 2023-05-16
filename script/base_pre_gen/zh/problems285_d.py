#问题陈述
#你运行一个有N个用户的网络服务。
#拥有当前句柄S_i的第i个用户想把它改成T_i。
#这里，S_1,...,和S_N是成对独立的，T_1,...,和T_N也是。
#确定是否有一个合适的顺序来改变他们的句柄，以满足他们所有的请求，但要符合以下条件：
#你一次只能改变一个用户的句柄；
#你对每个用户的句柄只改变一次；
#当改变句柄时，新的句柄不应该被其他用户在这一点上使用。
#
#限制条件
#1 ≦ N ≦ 10^5
#S_i和T_i是由小写英文字母组成的长度在1到8之间（含）的字符串。
#S_i ≠ T_i
#S_i是成对独立的。
#T_i是成对独立的。
#
#输入
#输入来自标准输入，格式如下：
#N
#S_1 T_1
#S_2 T_2
#.
#.
#.
#S_N T_N
#
#输出
#如果他们能改变他们的手柄以满足他们所有的请求，在符合条件的情况下，打印Yes；否则打印No。
#
#输入样本 1
#2
#b m
#m d
#
#样本输出1
#是
#拥有当前手柄b的第1个用户想把它改成m。
#第2个用户有一个当前的句柄m，想把它改成d。
#首先，你把第2个用户的句柄从m改成d；
#然后你把第1个用户的句柄从b改成m。这样，你就可以实现目标。
#注意，你不能一开始就把第1个用户的句柄改成m，因为这时它被第2个用户使用。
#
#输入样本 2
#3
#a b
#b c
#c a
#
#样本输出2
#不
#第1个拥有当前手柄a的用户想把它改成b。
#第2个用户用当前的手柄b想把它改成c。
#拥有当前句柄c的第3个用户想把它改成a。
#我们不能在条件允许的情况下改变他们的手柄。
#
#样本输入3
#5
#aaa bbb
#yyy zzz
#ccc ddd
#xxx yyy
#bbb ccc
#
#样本输出3
#是

def 