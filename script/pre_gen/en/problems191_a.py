#Problem Statement
#Takahashi and Aoki are playing baseball. Takahashi is the pitcher, and Aoki is the batter.
#Takahashi can throw an invisible pitch. When he throws it, the ball moves linearly at a constant speed V  [m / s], and it becomes invisible between the moment T seconds after throwing and the moment S seconds after throwing (inclusive). The ball keeps moving when it is invisible.
#If the ball is not invisible at the moment the ball is exactly D  m away from Takahashi, Aoki can hit the ball. Otherwise, he cannot hit it.
#Can Aoki hit the ball?
#
#Constraints
#1 ≦ V ≦ 1000
#1 ≦ T < S ≦ 1000
#1 ≦ D ≦ 1000
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#V T S D
#
#Output
#If Aoki can hit the ball, print Yes; otherwise, print No.
#
#Sample Input 1
#10 3 5 20
#
#Sample Output 1
#Yes
#The ball is exactly 20  m away from Takahashi at 2 seconds after throwing.
#On the other hand, the ball becomes invisible between 3 and 5 seconds (inclusive) after throwing, so Aoki can hit the ball.
#
#Sample Input 2
#10 3 5 30
#
#Sample Output 2
#No
#Note that the ball is also invisible at T seconds and S seconds after throwing.
#Here, the ball is exactly D  m away from Takahashi at T seconds after throwing, so the ball is invisible and cannot be hit by Aoki.

def 