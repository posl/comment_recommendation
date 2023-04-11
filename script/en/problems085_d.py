#Problem Statement
#You are going out for a walk, when you suddenly encounter a monster. Fortunately, you have N katana (swords), Katana 1, Katana 2, …, Katana N, and can perform the following two kinds of attacks in any order:
#Wield one of the katana you have. When you wield Katana i (1 ≤ i ≤ N), the monster receives a_i points of damage. The same katana can be wielded any number of times.
#Throw one of the katana you have. When you throw Katana i (1 ≤ i ≤ N) at the monster, it receives b_i points of damage, and you lose the katana. That is, you can no longer wield or throw that katana.
#The monster will vanish when the total damage it has received is H points or more. At least how many attacks do you need in order to vanish it in total?
#
#Constraints
#1 ≤ N ≤ 10^5
#1 ≤ H ≤ 10^9
#1 ≤ a_i ≤ b_i ≤ 10^9
#All input values are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N H
#a_1 b_1
#:
#a_N b_N
#
#Output
#Print the minimum total number of attacks required to vanish the monster.
#
#Sample Input 1
#1 10
#3 5
#
#Sample Output 1
#3
#You have one katana. Wielding it deals 3 points of damage, and throwing it deals 5 points of damage. By wielding it twice and then throwing it, you will deal 3 + 3 + 5 = 11 points of damage in a total of three attacks, vanishing the monster.
#
#Sample Input 2
#2 10
#3 5
#2 6
#
#Sample Output 2
#2
#In addition to the katana above, you also have another katana. Wielding it deals 2 points of damage, and throwing it deals 6 points of damage. By throwing both katana, you will deal 5 + 6 = 11 points of damage in two attacks, vanishing the monster.
#
#Sample Input 3
#4 1000000000
#1 1
#1 10000000
#1 30000000
#1 99999999
#
#Sample Output 3
#860000004
#
#Sample Input 4
#5 500
#35 44
#28 83
#46 62
#31 79
#40 43
#
#Sample Output 4
#9

def 