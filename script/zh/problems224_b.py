#问题陈述
#我们有一个有H个横行和W个纵列的网格，每个方格都包含一个整数。
#写在从上往下第i行和从左往下第j列的方格上的整数是A_{i, j}。
#请判断该方格是否满足以下条件。
#A_{i_1, j_1}+ A_{i_2, j_2} ≦ A_{i_2, j_1}+ A_{i_1, j_2}对每一个四元整数（i_1, i_2, j_1, j_2）都成立，使得1 ≦ i_1 < i_2 ≦ H，1 ≦ j_1 < j_2 ≦ W。
#
#约束条件
#2 ≦ H, W ≦ 50
#1 ≦ A_{i, j} ≦ 10^9
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#H W
#A_{1, 1} A_{1, 2} ...A_{1, W}
#A_{2, 1} A_{2, 2} ...A_{2, W}
#.
#.
#.
#A_{H, 1} A_{H, 2} ...A_{H, W}
#
#输出
#如果网格满足问题陈述中的条件，打印Yes；否则，打印No。
#
#输入样本 1
#3 3
#2 1 4
#3 1 3
#6 4 1
#
#样本输出1
#是
#有九个整数的四元组（i_1, i_2, j_1, j_2），使得1 ≦ i_1 < i_2 ≦ H，1 ≦ j_1 < j_2 ≦ W。+ A_{i_2, j_2} ≦ A_{i_2, j_1}+ A_{i_1, j_2}成立。下面是一些例子。
#对于（i_1, i_2, j_1, j_2）=（1, 2, 1, 2），我们有 A_{i_1, j_1}+ A_{i_2, j_2} = 2 + 1 ≦ 3 + 1 = A_{i_2, j_1}.+ A_{i_1, j_2}。
#对于（i_1, i_2, j_1, j_2）=（1, 2, 1, 3），我们有A_{i_1, j_1}。+ A_{i_2, j_2} = 2 + 3 ≦ 3 + 4 = A_{i_2, j_1}.+ A_{i_1, j_2}。
#对于（i_1, i_2, j_1, j_2）=（1, 2, 2, 3），我们有A_{i_1, j_1}。+ A_{i_2, j_2} = 1 + 3 ≦ 1 + 4 = A_{i_2, j_1}.+ A_{i_1, j_2}。
#对于（i_1, i_2, j_1, j_2）=（1, 3, 1, 2），我们有A_{i_1, j_1}。+ A_{i_2, j_2} = 2 + 4 ≦ 6 + 1 = A_{i_2, j_1}.+ A_{i_1, j_2}。
#对于（i_1, i_2, j_1, j_2）=（1, 3, 1, 3），我们有A_{i_1, j_1}。+ A_{i_2, j_2} = 2 + 1 ≦ 6 + 4 = A_{i_2, j_1}.+ A_{i_1, j_2}。
#我们还可以看到，该属性对其他四元组也是成立的：(i_1, i_2, j_1, j_2) = (1, 3, 2, 3), (2, 3, 1, 2), (2, 3, 1, 3) , (2, 3, 2, 3)。
#因此，我们应该打印是。
#
#输入样本 2
#2 4
#4 3 2 1
#5 6 7 8
#
#样本输出2
#不
#我们应该打印No，因为条件没有得到满足。
#这是因为，例如，我们有A_{i_1, j_1} + A_{i_2, j_2} = 4 + 8 = A_{i_2, j_1}。+ A_{i_2, j_2} = 4 + 8 > 5 + 1 = A_{i_2, j_1}.+ A_{i_1, j_2}对于（i_1, i_2, j_1, j_2）=（1, 2, 1, 4）。

def 