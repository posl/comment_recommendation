#Problem Statement
#You are given a matrix A with H_1 rows and W_1 columns, and a matrix B with H_2 rows and W_2 columns.
#For all integer pairs (i, j) such that 1 ≦ i ≦ H_1 and 1 ≦ j ≦ W_1, the element at the i-th row and j-th column of matrix A is A_{i, j}.
#For all integer pairs (i, j) such that 1 ≦ i ≦ H_2 and 1 ≦ j ≦ W_2, the element at the i-th row and j-th column of matrix B is B_{i, j}.
#You may perform the following operations on the matrix A any number of (possibly 0) times in any order:
#Choose an arbitrary row of A and remove it.
#Choose an arbitrary column of A and remove it.
#Determine if it is possible to make the matrix A equal the matrix B.
#
#Constraints
#1 ≦ H_2 ≦ H_1 ≦ 10
#1 ≦ W_2 ≦ W_1 ≦ 10
#1 ≦ A_{i, j} ≦ 10^9
#1 ≦ B_{i, j} ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#H_1 W_1
#A_{1, 1} A_{1, 2} ... A_{1, W_1}
#A_{2, 1} A_{2, 2} ... A_{2, W_1}
#.
#.
#.
#A_{H_1, 1} A_{H_1, 2} ... A_{H_1, W_1}
#H_2 W_2
#B_{1, 1} B_{1, 2} ... B_{1, W_2}
#B_{2, 1} B_{2, 2} ... B_{2, W_2}
#.
#.
#.
#B_{H_2, 1} B_{H_2, 2} ... B_{H_2, W_2}
#
#Output
#Print Yes if it is possible to make the matrix A equal the matrix B;
#print No otherwise.
#Note that the judge is case-sensitive.
#
#Sample Input 1
#4 5
#1 2 3 4 5
#6 7 8 9 10
#11 12 13 14 15
#16 17 18 19 20
#2 3
#6 8 9
#16 18 19
#
#Sample Output 1
#Yes
#Removing the 2-nd column from the initial A results in:
#1 3 4 5
#6 8 9 10
#11 13 14 15
#16 18 19 20
#Then, removing the 3-rd row from A results in:
#1 3 4 5
#6 8 9 10
#16 18 19 20
#Then, removing the 1-st row from A results in:
#6 8 9 10
#16 18 19 20
#Then, removing the 4-th column from A results in:
#6 8 9
#16 18 19
#Now the matrix equals the matrix B.
#Thus, we can make the matrix A equal the matrix B by repeating the operations, so Yes should be printed.
#
#Sample Input 2
#3 3
#1 1 1
#1 1 1
#1 1 1
#1 1
#2
#
#Sample Output 2
#No
#Regardless of how we perform the operations, we cannot make the matrix A equal the matrix B,
#so No should be printed.

def 