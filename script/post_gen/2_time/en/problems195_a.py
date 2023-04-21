#Problem Statement
#Takahashi, the magician, is fighting with a monster.
#His magic can defeat a monster whose health is a multiple of M. It has no effect on a monster whose health is not a multiple of M.
#Can his magic defeat a monster whose health is H?
#
#Constraints
#1 ≦ M ≦ 1000
#1 ≦ H ≦ 1000
#M and H are integers.
#
#Input
#Input is given from Standard Input in the following format:
#M H
#
#Output
#If Takahashi's magic can defeat the monster, print Yes; otherwise, print No.
#
#Sample Input 1
#10 120
#
#Sample Output 1
#Yes
#Takahashi's magic can defeat a monster whose health is a multiple of 10.
#120 is a multiple of 10, so his magic can defeat the monster with health 120.
#
#Sample Input 2
#10 125
#
#Sample Output 2
#No
#125 is not a multiple of 10, so his magic cannot defeat the monster with health 125.

def 