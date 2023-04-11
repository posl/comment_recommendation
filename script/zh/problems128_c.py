#问题陈述
#我们有N个具有 "开 "和 "关 "状态的开关，以及M个灯泡。开关的编号是1到N，灯泡的编号是1到M。
#灯泡i与k_i个开关相连：开关s_{i1}，s_{i2}，...，和s_{ik_i}。当这些开关中 "开 "的开关数与p_i的模数一致时，它就被点亮。
#有多少种开关的 "开 "和 "关 "状态的组合可以点亮所有的灯泡？
#
#限制条件
#1 ≦ N, M ≦ 10
#1 ≦ k_i ≦ N
#1 ≦ s_{ij} ≦ N
#s_{ia}≠ s_{ib} (a ≠ b)
#p_i为0或1。
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入给出的，格式如下：
#N M
#k_1 s_{11} s_{12}...s_{1k_1}
#:
#k_M s_{M1} s_{M2} ... s_{Mk_M} 。
#p_1 p_2 ... p_M
#
#输出
#打印能点亮所有灯泡的开关的 "开 "和 "关 "状态的组合数。
#
#输入样本 1
#2 2
#2 1 2
#1 2
#0 1
#
#样本输出1
#1
#当下列开关中存在偶数个 "打开 "时，灯泡1被点亮：开关1和2。
#当下列开关中有奇数个 "打开 "时，灯泡2被点亮：开关2。
#开关1、开关2）的状态有四种可能的组合：(开，开），（开，关），（关，开）和（关，关）。其中，只有（开，开）能点亮所有的灯泡，所以我们应该打印1。
#
#输入样本 2
#2 3
#2 1 2
#1 1
#1 2
#0 0 1
#
#样本输出2
#0
#当下列开关中存在偶数个 "打开 "时，灯泡1被点亮：开关1和2。
#当下列开关中有偶数个 "打开 "时，灯泡2被点亮：开关1。
#当下列开关中有奇数个 "打开 "时，灯泡3会被点亮：开关2。
#开关1必须 "关闭 "才能点亮灯泡2，开关2必须 "打开 "才能点亮灯泡3，但这样灯泡1就不会被点亮。因此，不存在能点亮所有灯泡的开关状态组合，所以我们应该打印0。
#
#输入样本 3
#5 2
#3 1 2 5
#2 2 3
#1 0
#
#样本输出3
#8

def 