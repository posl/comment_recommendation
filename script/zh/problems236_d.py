#问题陈述
#2N个编号为1，2，...，2N的人参加一个舞会。
#他们将分组为N对，并进行舞蹈。
#如果i号人和j号人配对，其中i号人小于j号人，则该配对的亲密度为A_{i, j}。
#如果N对人的亲和力为B_1, B_2, ..., B_N，那么球的总乐趣就是它们的比特XOR：B_1⊕B_2⊕...⊕B_N。
#当2N个人可以自由组合成N对时，打印出球的最大可能的总乐趣。
#
#限制条件
#1 ≦ N ≦ 8
#0 ≦ A_{i，j}< 2^{30}
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入给出的，格式如下：
#N
#A_{1, 2} A_{1, 3} A_{1, 4} ...A_{1, 2N}
#A_{2, 3} A_{2, 4} ...A_{2, 2N}
#A_{3, 4} ...A_{3, 2N}
#.
#.
#.
#A_{2N-1, 2N}
#
#输出
#打印该球的最大可能的总乐趣。
#
#输入样本 1
#2
#4 0 1
#5 3
#2
#
#样本输出1
#6
#让{i, j}表示一对人i和人j。
#四个人有三种方式可以分组为两对，如下所示。
#分组为{1，2}，{3，4}。
#这里的球的总乐趣是A_{1，2}⊕A_{3，4}=4⊕2=6。
#分组为{1，3}，{2，4}。
#这里的球的总乐趣是A_{1, 3} ⊕ A_{2, 4} = 0 ⊕ 3 = 3。
#分组为{1，4}，{2，3}。
#这里的球的总乐趣是A_{1, 4} ⊕ A_{2, 3} = 1 ⊕ 5 = 4。
#因此，球的最大可能的总乐趣是6。
#
#输入样本2
#1
#5
#
#采样输出2
#5
#将只有一对人1和人2，其中球的总乐趣是5。
#
#样本输入3
#5
#900606388 317329110 665451442 1045743214 260775845 726039763 57365372 741277060 944347467
#369646735 642395945 599952146 86221147 523579390 591944369 911198494 695097136
#138172503 571268336 111747377 595746631 934427285 840101927 757856472
#655483844 580613112 445614713 607825444 252585196 725229185
#827291247 105489451 58628521 1032791417 152042357
#919691140 703307785 100772330 370415195
#666350287 691977663 987658020
#1039679956 218233643
#70938785
#
#样本输出3
#1073289207

def 