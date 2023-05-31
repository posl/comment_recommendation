#问题陈述
#你有N根竹子。这些竹子的长度（以厘米为单位）分别为l_1，l_2，...，l_N。
#你的目标是用这些竹子中的一部分（可能是全部）来获得长度为A、B、C的三根竹子。为此，你可以使用以下三种魔法的任意数量：
#延伸魔法：消耗1MP（魔法点）。选择一根竹子，将其长度增加1。
#缩短魔法：消耗1MP。选择一根长度至少为2的竹子，减少其长度1。
#组成魔法：消耗10MP。选择两根竹子并将它们合并成一根竹子。这个新竹子的长度等于两根竹子的长度之和。(之后，可以对这根竹子使用更多的魔法）。
#至少需要多少MP才能达到目的？
#
#限制条件
#3 ≦ N ≦ 8
#1 ≦ c < b < a ≦ 1000
#1 ≦ l_i ≦ 1000
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#N A B C
#l_1
#l_2
#:
#l_N
#
#输出
#打印实现目标所需的最小MP量。
#
#输入样本1
#5 100 90 80
#98
#40
#30
#21
#80
#
#样本输出1
#23
#我们要从98、40、30、21、80这五根竹子中获得长度为100、90、80的三根竹子。我们已经有了一根长度为80的竹子，我们可以通过使用以下魔法获得长度为100、90的竹子，总花费为23MP，这是最佳的。
#对长度为98的竹子使用两次延伸魔法，获得长度为100的竹子。(消耗的MP: 2)
#对长度为40，30的竹子使用组成魔法，得到一根长度为70的竹子。(消耗的MP: 10)
#对长度为21的竹子使用一次缩短魔法，获得长度为20的竹子。(消耗的MP: 1)
#对步骤2中得到的长度为70的竹子和步骤3中得到的长度为20的竹子使用组合魔法，得到长度为90的竹子。(消耗的MP: 10)
#
#输入样本2
#8 100 90 80
#100
#100
#90
#90
#90
#80
#80
#80
#
#样本输出2
#0
#如果我们已经有了所需长度的所有竹子，那么需要的MP数量是0。
#
#输入样本3
#8 1000 800 100
#300
#333
#400
#444
#500
#555
#600
#666
#
#样本输出3
#243

def 