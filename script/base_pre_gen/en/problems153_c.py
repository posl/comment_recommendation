#Problem Statement
#Fennec is fighting with N monsters.
#The health of the i-th monster is H_i.
#Fennec can do the following two actions:
#Attack: Fennec chooses one monster. That monster's health will decrease by 1.
#Special Move: Fennec chooses one monster. That monster's health will become 0.
#There is no way other than Attack and Special Move to decrease the monsters' health.
#Fennec wins when all the monsters' healths become 0 or below.
#Find the minimum number of times Fennec needs to do Attack (not counting Special Move) before winning when she can use Special Move at most K times.
#
#Constraints
#1 ≦ N ≦ 2 × 10^5
#0 ≦ K ≦ 2 × 10^5
#1 ≦ H_i ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N K
#H_1 ... H_N
#
#Output
#Print the minimum number of times Fennec needs to do Attack (not counting Special Move) before winning.
#
#Sample Input 1
#3 1
#4 1 5
#
#Sample Output 1
#5
#By using Special Move on the third monster, and doing Attack four times on the first monster and once on the second monster, Fennec can win with five Attacks.
#
#Sample Input 2
#8 9
#7 9 3 2 3 8 4 6
#
#Sample Output 2
#0
#She can use Special Move on all the monsters.
#
#Sample Input 3
#3 0
#1000000000 1000000000 1000000000
#
#Sample Output 3
#3000000000
#Watch out for overflow.

def 