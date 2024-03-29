#Problem Statement
#There is a device with a screen that shows a single-digit number, and a button.  
#When the screen is showing a number k, pressing the button once changes the number on the screen to a_k.  
#The device currently shows 0.  After pressing the button 3 times, what will be shown on the screen?
#
#Constraints
#0≦ a_i ≦ 9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#a_0 a_1 ... a_9
#
#Output
#Print the answer.  
#
#Sample Input 1
#9 0 1 2 3 4 5 6 7 8
#
#Sample Output 1
#7
#The number on the screen transitions as 0 -> 9 -> 8 -> 7.  
#
#Sample Input 2
#4 8 8 8 0 8 8 8 8 8
#
#Sample Output 2
#4
#The number on the screen transitions as 0 -> 4 -> 0 -> 4.  
#
#Sample Input 3
#0 0 0 0 0 0 0 0 0 0
#
#Sample Output 3
#0

def 