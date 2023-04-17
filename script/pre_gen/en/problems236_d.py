#Problem Statement
#2N people numbered 1, 2, ..., 2N attend a ball.
#They will group into N pairs and have a dance.
#If Person i and Person j pair up, where i is smaller than j, the affinity of that pair is A_{i, j}.
#If the N pairs have the affinity of B_1, B_2, ..., B_N, the total fun of the ball is the bitwise XOR of them: B_1 ⊕ B_2 ⊕ ... ⊕ B_N.
#Print the maximum possible total fun of the ball when the 2N people can freely group into N pairs.
#
#Constraints
#1 ≦ N ≦ 8
#0 ≦ A_{i, j} < 2^{30}
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_{1, 2} A_{1, 3} A_{1, 4} ... A_{1, 2N}
#A_{2, 3} A_{2, 4} ... A_{2, 2N}
#A_{3, 4} ... A_{3, 2N}
#.
#.
#.
#A_{2N-1, 2N}
#
#Output
#Print the maximum possible total fun of the ball.
#
#Sample Input 1
#2
#4 0 1
#5 3
#2
#
#Sample Output 1
#6
#Let {i, j} denote a pair of Person i and Person j.
#There are three ways for the four people to group into two pairs, as follows.
#Group into {1, 2}, {3, 4}.
#The total fun of the ball here is A_{1, 2} ⊕ A_{3, 4} = 4 ⊕ 2 = 6.
#Group into {1, 3}, {2, 4}.
#The total fun of the ball here is A_{1, 3} ⊕ A_{2, 4} = 0 ⊕ 3 = 3.
#Group into {1, 4}, {2, 3}.
#The total fun of the ball here is A_{1, 4} ⊕ A_{2, 3} = 1 ⊕ 5 = 4.
#Therefore, the maximum possible total fun of the ball is 6.
#
#Sample Input 2
#1
#5
#
#Sample Output 2
#5
#There will be just a pair of Person 1 and Person 2, where the total fun of the ball is 5.
#
#Sample Input 3
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
#Sample Output 3
#1073289207

def 