#Problem Statement
#There are a total of A + B cats and dogs.
#Among them, A are known to be cats, but the remaining B are not known to be either cats or dogs.
#Determine if it is possible that there are exactly X cats among these A + B animals.
#
#Constraints
#1 ≦ A ≦ 100
#1 ≦ B ≦ 100
#1 ≦ X ≦ 200
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#A B X
#
#Output
#If it is possible that there are exactly X cats, print YES; if it is impossible, print NO.
#
#Sample Input 1
#3 5 4
#
#Sample Output 1
#YES
#If there are one cat and four dogs among the B = 5 animals, there are X = 4 cats in total.
#
#Sample Input 2
#2 2 6
#
#Sample Output 2
#NO
#Even if all of the B = 2 animals are cats, there are less than X = 6 cats in total.
#
#Sample Input 3
#5 3 2
#
#Sample Output 3
#NO
#Even if all of the B = 3 animals are dogs, there are more than X = 2 cats in total.

def 