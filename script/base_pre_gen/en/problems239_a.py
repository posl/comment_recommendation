#Problem Statement
#Assuming that the horizon seen from a place x meters above the ground is (x(12800000+x))^(1/2) meters away,
#find how many meters away the horizon seen from a place H meters above the ground is.
#
#Constraints
#1 ≦ H ≦ 10^5
#H is an integer.
#
#Input
#Input is given from Standard Input in the following format:
#H
#
#Output
#Print the answer.
#Your answer will be considered correct when the absolute or relative error from the judge's answer is at most 10^{-6}.
#
#Sample Input 1
#333
#
#Sample Output 1
#65287.907678222
#We have (333(12800000+333))^(1/2) = 65287.9076782....  Outputs such as 65287.91 would also be accepted.
#
#Sample Input 2
#634
#
#Sample Output 2
#90086.635834623
#We have (634(12800000+634))^(1/2) = 90086.6358346....

def 