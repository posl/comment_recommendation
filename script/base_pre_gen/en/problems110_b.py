#Problem Statement
#Our world is one-dimensional, and ruled by two empires called Empire A and Empire B.
#The capital of Empire A is located at coordinate X, and that of Empire B is located at coordinate Y.
#One day, Empire A becomes inclined to put the cities at coordinates x_1, x_2, ..., x_N under its control, and Empire B becomes inclined to put the cities at coordinates y_1, y_2, ..., y_M under its control.
#If there exists an integer Z that satisfies all of the following three conditions, they will come to an agreement, but otherwise war will break out.
#X < Z ≦ Y
#x_1, x_2, ..., x_N < Z
#y_1, y_2, ..., y_M ≧ Z
#Determine if war will break out.
#
#Constraints
#All values in input are integers.
#1 ≦ N, M ≦ 100
#-100 ≦ X < Y ≦ 100
#-100 ≦ x_i, y_i ≦ 100
#x_1, x_2, ..., x_N ≠ X
#x_i are all different.
#y_1, y_2, ..., y_M ≠ Y
#y_i are all different.
#
#Input
#Input is given from Standard Input in the following format:
#N M X Y
#x_1 x_2 ... x_N
#y_1 y_2 ... y_M
#
#Output
#If war will break out, print War; otherwise, print No War.
#
#Sample Input 1
#3 2 10 20
#8 15 13
#16 22
#
#Sample Output 1
#No War
#The choice Z = 16 satisfies all of the three conditions as follows, thus they will come to an agreement.
#X = 10 < 16 ≦ 20 = Y
#8, 15, 13 < 16
#16, 22 ≧ 16
#
#Sample Input 2
#4 2 -48 -1
#-20 -35 -91 -23
#-22 66
#
#Sample Output 2
#War
#
#Sample Input 3
#5 3 6 8
#-10 3 1 5 -100
#100 6 14
#
#Sample Output 3
#War

def 