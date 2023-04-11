#问题说明
#对于一个基数X，它乘以Y次方的乘积被称为X到Y次方，表示为pow(X, Y)。
#例如，我们有pow(2,3)=2×2×2=8。
#给出三个整数A、B和C，比较pow(A,C)和pow(B,C)以确定哪个更大。
#
#限制条件
#-10^9 ≦ A,B ≦ 10^9
#1 ≦ C ≦ 10^9
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#A B C
#
#输出
#如果pow(A,C)<pow(B,C)，打印<；如果pow(A,C)>pow(B,C)，打印>；如果pow(A,C)=pow(B,C)，打印=。
#
#输入样本 1
#3 2 4
#
#输出示例 1
#>
#我们有 pow(3,4)=81 和 pow(2,4)=16。
#
#样本输入2
#-7 7 2
#
#样本输出2
#=
#我们有 pow(-7,2)=49 和 pow(7,2)=49。
#
#样本输入3
#-8 6 3
#
#样本输出3
#<
#我们有 pow(-8,3)=-512 和 pow(6,3)=216。

def 