#Problem Statement
#There are N people numbered 1, 2, ..., N in the xy-plane. Person i is at the coordinates (X_i, Y_i).
#K of these people, Persons A_1, A_2, ..., A_K, will receive lights of the same strength.
#When a person at coordinates (x, y) has a light of strength R, it lights up the interior of a circle of radius R centered at (x, y) (including the boundary).
#Find the minimum strength of the lights needed for every person to be lit by at least one light.  
#
#Constraints
#All values in input are integers.
#1 ≦ K < N ≦ 1000
#1 ≦ A_1 < A_2 < ... < A_K ≦ N
#|X_i|,|Y_i| ≦ 10^5
#(X_i,Y_i) ≠ (X_j,Y_j), if i ≠ j.
#
#Input
#Input is given from Standard Input in the following format:
#N K
#A_1 A_2 ... A_K
#X_1 Y_1
#X_2 Y_2
#.
#.
#.
#X_N Y_N
#
#Output
#Print the answer as a real number.
#Your output will be considered correct if its absolute or relative error from the judge's output is at most 10^{-5}.
#
#Sample Input 1
#4 2
#2 3
#0 0
#0 1
#1 2
#2 0
#
#Sample Output 1
#2.23606797749978969
#This input contains four people. Among them, Persons 2 and 3 will have lights.
#Every person will be lit by at least one light if R ≧ (5)^(1/2) ≈ 2.236068.
#
#Sample Input 2
#2 1
#2
#-100000 -100000
#100000 100000
#
#Sample Output 2
#282842.712474619009
#
#Sample Input 3
#8 3
#2 6 8
#-17683 17993
#93038 47074
#58079 -57520
#-41515 -89802
#-72739 68805
#24324 -73073
#71049 72103
#47863 19268
#
#Sample Output 3
#130379.280458974768

def 