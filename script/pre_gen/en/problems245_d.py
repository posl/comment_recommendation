#Problem Statement
#We have a polynomial of degree N, A(x)=A_Nx^N+A_{N-1}x^{N-1}+... +A_1x+A_0,
#and another of degree M, B(x)=B_Mx^M+B_{M-1}x^{M-1}+... +B_1x+B_0.
#Here, each coefficient of A(x) and B(x) is an integer whose absolute value is at most 100, and the leading coefficients are not 0.
#Also, let the product of them be C(x)=A(x)B(x)=C_{N+M}x^{N+M}+C_{N+M-1}x^{N+M-1}+... +C_1x+C_0.
#Given A_0,A_1,..., A_N and C_0,C_1,..., C_{N+M}, find B_0,B_1,..., B_M.
#Here, the given inputs guarantee that there is a unique sequence B_0, B_1, ..., B_M that satisfies the given conditions.
#
#Constraints
#1 ≦ N < 100
#1 ≦ M < 100
#|A_i| ≦ 100
#|C_i| ≦ 10^6
#A_N ≠ 0
#C_{N+M} ≠ 0
#There is a unique sequence B_0, B_1, ..., B_M that satisfies the conditions given in the statement.
#
#Input
#Input is given from Standard Input in the following format:
#N M
#A_0 A_1 ... A_{N-1} A_N
#C_0 C_1 ... C_{N+M-1} C_{N+M}
#
#Output
#Print the M+1 integers B_0,B_1,..., B_M in one line, with spaces in between.
#
#Sample Input 1
#1 2
#2 1
#12 14 8 2
#
#Sample Output 1
#6 4 2
#For A(x)=x+2 and B(x)=2x^2+4x+6, we have C(x)=A(x)B(x)=(x+2)(2x^2+4x+6)=2x^3+8x^2+14x+12, so B(x)=2x^2+4x+6 satisfies the given conditions. Thus, B_0=6, B_1=4, B_2=2 should be printed in this order, with spaces in between.
#
#Sample Input 2
#1 1
#100 1
#10000 0 -1
#
#Sample Output 2
#100 -1
#We have A(x)=x+100, C(x)=-x^2+10000, for which B(x)=-x+100 satisfies the given conditions.
#Thus, 100, -1 should be printed in this order, with spaces in between.

def 