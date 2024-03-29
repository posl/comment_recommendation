#Problem Statement
#Takahashi, the magician, is fighting with a monster.
#He can use N spells.
#The i-th spell takes X_i seconds to cast and has a power Y_i.
#However, the monster is strong enough to avoid taking damage from spells taking S or more seconds to cast and spells with powers D or less.
#Also, there is nothing other than spells that can do damage to the monster.
#Can Takahashi do damage to the monster?  
#
#Constraints
#All values in input are integers.
#1 ≤ N ≤ 100
#1 ≤ X_i ≤ 10^9
#1 ≤ Y_i ≤ 10^9
#1 ≤ S ≤ 10^9
#1 ≤ D ≤ 10^9
#
#Input
#Input is given from Standard Input in the following format:
#N S D
#X_1 Y_1
#.
#.
#.
#X_N Y_N
#
#Output
#If Takahashi can do damage to the monster, print Yes; otherwise, print No.
#
#Sample Input 1
#4 9 9
#5 5
#15 5
#5 15
#15 15
#
#Sample Output 1
#Yes
#The second and fourth spells take too much time to do damage.
#Also, the first and second spells do not have enough powers to do damage.
#Thus, only the third spell can do damage.
#
#Sample Input 2
#3 691 273
#691 997
#593 273
#691 273
#
#Sample Output 2
#No
#
#Sample Input 3
#7 100 100
#10 11
#12 67
#192 79
#154 197
#142 158
#20 25
#17 108
#
#Sample Output 3
#Yes
#Only the seventh spell can do damage.

def 