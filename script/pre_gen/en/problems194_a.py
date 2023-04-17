#Problem Statement
#In Japan, there are four major categories of ice cream type products:
#an ice cream type product with at least 15 percent milk solids and at least 8 percent milk fat is called an ice cream;
#an ice cream type product with at least 10 percent milk solids and at least 3 percent milk fat that is not an ice cream is called an ice milk;
#an ice cream type product with at least 3 percent milk solids that is not an ice cream or an ice milk is called a lacto ice;
#an ice cream type product that is not an ice cream, an ice milk, or a lacto ice is called a flavored ice.
#Here, milk solids consist of milk fat and milk solids-not-fat.
#AtCoder's famous product Snuke Ice contains A percent milk solids-not-fat and B percent milk fat.
#Which of the categories above does Snuke Ice fall into?
#Print your answer as an integer according to the Output section.
#
#Constraints
#0 ≦ A ≦ 100
#0 ≦ B ≦ 100
#A + B ≦ 100
#A and B are integers.
#
#Input
#Input is given from Standard Input in the following format:
#A B
#
#Output
#Print an integer as follows:
#if Snuke Ice is an ice cream, print 1;
#if Snuke Ice is an ice milk, print 2;
#if Snuke Ice is a lacto ice, print 3;
#if Snuke Ice is a flavored ice, print 4.
#
#Sample Input 1
#10 8
#
#Sample Output 1
#1
#This product contains 10 percent milk solids-not-fat and 8 percent milk fat, for a total of 18 percent milk solids.
#Since it contains not less than 15 percent milk solids and not less than 8 percent milk fat, it is an ice cream; the correct output is 1.
#
#Sample Input 2
#1 2
#
#Sample Output 2
#3
#Since it contains exactly 3 percent milk solids, it is not an ice cream or an ice milk but is a lacto ice; the correct output is 3.
#
#Sample Input 3
#0 0
#
#Sample Output 3
#4
#It is a flavored ice.

def 