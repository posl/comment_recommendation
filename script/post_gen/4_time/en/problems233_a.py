#Problem Statement
#Takahashi wants to send a letter to Santa Claus. He has an envelope with an X-yen (Japanese currency) stamp stuck on it.
#To be delivered to Santa Claus, the envelope must have stamps in a total value of at least Y yen.
#Takahashi will put some more 10-yen stamps so that the envelope will have stamps worth at least Y yen in total.
#At least how many more 10-yen stamps does Takahashi need to put on the envelope?
#
#Constraints
#X and Y are integers.
#1 ≦ X,Y ≦ 1000
#
#Input
#Input is given from Standard Input in the following format:
#X Y
#
#Output
#Print the answer as an integer.
#
#Sample Input 1
#80 94
#
#Sample Output 1
#2
#After adding zero 10-yen stamps to the 80-yen stamp, the total is 80 yen, which is less than the required amount of 94 yen.
#After adding one 10-yen stamp to the 80-yen stamp, the total is 90 yen, which is less than the required amount of 94 yen.
#After adding two 10-yen stamps to the 80-yen stamp, the total is 100 yen, which is not less than the required amount of 94 yen.
#
#Sample Input 2
#1000 63
#
#Sample Output 2
#0
#The envelope may already have a stamp with enough value.
#
#Sample Input 3
#270 750
#
#Sample Output 3
#48

def 