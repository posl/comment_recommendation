#Problem Statement
#Takahashi turns on the light of his room at S o'clock (on the 24-hour clock) every day and turns it off at T o'clock every day.
#The date may change while the light is on.
#Determine whether the light is on at 30 minutes past X o'clock.
#
#Constraints
#0 ≦ S, T, X ≦ 23
#S ≠ T
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#S T X
#
#Output
#If the light is on at 30 minutes past X o'clock, print Yes; otherwise, print No.
#
#Sample Input 1
#7 20 12
#
#Sample Output 1
#Yes
#The light is on between 7 o'clock and 20 o'clock. At 30 minutes past 12 o'clock, it is on, so we print Yes. 
#
#Sample Input 2
#20 7 12
#
#Sample Output 2
#No
#The light is on between 0 o'clock and 7 o'clock, and between 20 o'clock and 0 o'clock (on the next day). At 30 minutes past 12 o'clock, it is off, so we print No. 
#
#Sample Input 3
#23 0 23
#
#Sample Output 3
#Yes

def 