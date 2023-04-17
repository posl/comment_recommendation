#Problem Statement
#A superman, Takahashi, is about to jump off the roof of a building to help a person in trouble on the ground.
#Takahashi's planet has a constant value g that represents the strength of gravity, and the time it takes for him to reach the ground after starting to fall is (A/((g)^(1/2))).
#It is now time 0, and g = 1.
#Takahashi will perform the following operation as many times as he wants (possibly zero).
#Use a superpower to increase the value of g by 1. This takes a time of B.
#Then, he will jump off the building. After starting to fall, he cannot change the value of g. Additionally, we only consider the time it takes to perform the operation and fall.
#Find the earliest time Takahashi can reach the ground.
#
#Constraints
#1 ≦ A ≦ 10^{18}
#1 ≦ B ≦ 10^{18}
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#A B
#
#Output
#Print the earliest time Takahashi can reach the ground.
#Your output will be accepted when its absolute or relative error from the true value is at most 10^{-6}.
#
#Sample Input 1
#10 1
#
#Sample Output 1
#7.7735026919
#If he performs the operation zero times, he will reach the ground at time 1× 0+((10)/((1)^(1/2))) = 10.
#If he performs the operation once, he will reach the ground at time 1× 1+((10)/((2)^(1/2))) ≒ 8.07.
#If he performs the operation twice, he will reach the ground at time 1× 2+((10)/((3)^(1/2))) ≒ 7.77.
#If he performs the operation three times, he will reach the ground at time 1× 3+((10)/((4)^(1/2))) = 8.
#Performing the operation four or more times will only delay the time to reach the ground.
#Therefore, it is optimal to perform the operation twice before jumping off, and the answer is 2+((10)/((3)^(1/2))).
#
#Sample Input 2
#5 10
#
#Sample Output 2
#5.0000000000
#It is optimal not to perform the operation at all.
#
#Sample Input 3
#1000000000000000000 100
#
#Sample Output 3
#8772053214538.5976562500

def 