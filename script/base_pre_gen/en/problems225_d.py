#Problem Statement
#Takahashi is playing with toy trains, connecting and disconnecting them.
#There are N toy train cars, with car numbers: Car 1, Car 2, ..., Car N.
#Initially, all cars are separated.
#You will be given Q queries. Process them in the order they are given.
#There are three kinds of queries, as follows.
#1 x y: Connect the front of Car y to the rear of Car x.
#It is guaranteed that:
#x ≠ y
#just before this query, no train is connected to the rear of Car x;
#just before this query, no train is connected to the front of Car y;
#just before this query, Car x and Car y belong to different connected components.
#
#2 x y: Disconnect the front of Car y from the rear of Car x.
#It is guaranteed that:
#x ≠ y;
#just before this query, the front of Car y is directly connected to the rear of Car x.  
#
#3 x: Print the car numbers of the cars belonging to the connected component containing Car x, from front to back. 
#
#
#Constraints
#2 ≦ N ≦ 10^5
#1 ≦ Q ≦ 10^5
#1 ≦ x ≦ N
#1 ≦ y ≦ N
#All values in input are integers.
#All queries satisfy the conditions in the Problem Statement.
#The queries of the format 3 x ask to print at most 10^6 car numbers in total.
#
#Input
#Input is given from Standard Input in the following format:
#N Q
#query_1
#query_2
#.
#.
#.
#query_Q
#The i-th query query_i begins with an integer c_i (1, 2, or 3) representing the kind of the query, followed by x and y if c_i = 1 or 2, and followed by x if c_i = 3.
#In short, each query is in one of the following three formats:
#1 x y
#2 x y
#3 x
#
#Output
#If a query with c_i = 3 asks to print the values j_1, j_2, ..., j_M, output the following line:
#M j_1 j_2 ... j_M
#Your output should consist of q lines, where q is the number of queries with c_i = 3.
#The k-th line (1 ≦ k ≦ q) should contain the response to the k-th such query.
#
#Sample Input 1
#7 14
#1 6 3
#1 4 1
#1 5 2
#1 2 7
#1 3 5
#3 2
#3 4
#3 6
#2 3 5
#2 4 1
#1 1 5
#3 2
#3 4
#3 6
#
#Sample Output 1
#5 6 3 5 2 7
#2 4 1
#5 6 3 5 2 7
#4 1 5 2 7
#1 4
#2 6 3
#The figure below shows the cars when the first 5 queries are processed.
#For example, Car 2 belongs to the same connected component as Cars 3, 5, 6, 7, which is different from the connected component containing Cars 1, 4.
#The figure below shows the cars when the first 11 queries are processed.  

def 