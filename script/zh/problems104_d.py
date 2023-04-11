#问题陈述
#一个字符串T的ABC数是满足以下所有条件的整数（i, j, k）的三倍数：
#1 ≤ i < j < k ≤ |T| (|T|是T的长度。)
#T_i = A (T_i是T的第i个字符，从头开始。)
#T_j = B
#T_k = C
#例如，当T=ABCBC时，有三个满足条件的三倍整数（i, j, k）：（1, 2, 3），（1, 2, 5），（1, 4, 5）。因此，T的ABC数是3。
#给你一个字符串S，S的每个字符是A，B，C或?
#我们可以用A、B或C替换S中出现的每个字符，从而组成3^Q的字符串，求所有这些字符串的ABC号码之和。
#这个和可能非常大，所以要打印10^9+7的模数。
#
#限制条件
#3 ≤ |S| ≤ 10^5
#S的每个字符都是A、B、C或?
#
#输入
#输入来自标准输入，其格式如下：
#S
#
#輸出
#打印所有 3^Q 字符串的 ABC 数字之和，模数为 10^9 + 7。
#
#输入样本1
#A??C
#
#样本输出1
#8
#在这种情况下，Q=2，我们可以通过用A、B或C替换每一次出现的?来制作3^Q=9个字符串，这些字符串的ABC号码如下：
#AAAC：0
#AABC：2
#AACC：0
#ABAC：1
#ABBC：2
#ABCC: 2
#ACAC: 0
#ACBC：1
#ACCC：0
#这些的总和是0+2+0+1+2+2+0+1+0=8，所以我们打印8的模数10^9+7，也就是8。
#
#输入样本2
#ABCBC
#
#样本输出 2
#3
#当Q=0时，我们打印S本身的ABC号码，模数为10^9+7。这个字符串与问题陈述中作为例子给出的字符串相同，其ABC数为3。
#
#输入样本3
#????C?????B??????A???????
#
#样本输出3
#979596887
#在这种情况下，所有 3^Q 字符串的 ABC 数字之和是 2291979612924，我们应该打印这个数字的模数 10^9 + 7，即 979596887。

def 