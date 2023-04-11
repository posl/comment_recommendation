#问题陈述
#我们有一个袋子，里面有A金币，B银币，C铜币。
#直到袋子里有100个相同颜色的硬币，我们将重复以下操作：
#操作：随机从袋子里拿出一枚硬币。(每枚硬币被选中的概率相同。)然后，将两枚与取出的硬币相同的硬币放回袋中。
#求该操作次数的期望值。
#
#限制条件
#0 ≦ A,B,C ≦ 99
#A+B+C ≧ 1
#
#输入
#输入是由标准输入法提供的，格式如下：
#A B C
#
#輸出
#打印该操作次数的预期值。如果你的输出与正确值的绝对或相对误差最多为10^{-6}，你的输出将被接受。
#
#输入样本 1
#99 99 99
#
#样本输出1
#1.000000000
#无论我们在第一次操作中拿出什么硬币，袋子里都会有100个该种硬币。
#
#样本输入2
#98 99 99
#
#样本输出2
#1.331081081
#只有在第一次操作中拿出一枚金币，我们才会进行第二次操作。
#因此，预期的操作次数是2×（（98）/（98+99+99））+1×（（99）/（98+99+99））+1×（（99）/（98+99+99））=1.331081081...
#
#样本输入3
#0 0 1
#
#样本输出3
#99.000000000
#每次操作都会增加一枚铜币。
#
#样本输入4
#31 41 59
#
#输出样本4
#91.835008202

def 