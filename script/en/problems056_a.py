#Problem Statement
#Two deer, AtCoDeer and TopCoDeer, are playing a game called Honest or Dishonest.
#In this game, an honest player always tells the truth, and an dishonest player always tell lies.
#You are given two characters a and b as the input. Each of them is either H or D, and carries the following information:
#If a=H, AtCoDeer is honest; if a=D, AtCoDeer is dishonest.
#If b=H, AtCoDeer is saying that TopCoDeer is honest; if b=D, AtCoDeer is saying that TopCoDeer is dishonest.
#Given this information, determine whether TopCoDeer is honest.
#
#Constraints
#a=H or a=D.
#b=H or b=D.
#
#Input
#The input is given from Standard Input in the following format:
#a b
#
#Output
#If TopCoDeer is honest, print H. If he is dishonest, print D.
#
#Sample Input 1
#H H
#
#Sample Output 1
#H
#In this input, AtCoDeer is honest. Hence, as he says, TopCoDeer is honest.
#
#Sample Input 2
#D H
#
#Sample Output 2
#D
#In this input, AtCoDeer is dishonest. Hence, contrary to what he says, TopCoDeer is dishonest.
#
#Sample Input 3
#D D
#
#Sample Output 3
#H

def 