def main():
    N, Q = map(int, input().split())
    #N: number of toy train cars
    #Q: number of queries
    #initially, all cars are separated.
    #car numbers: Car 1, Car 2, ..., Car N.
    #1 x y: Connect the front of Car y to the rear of Car x.
    #2 x y: Disconnect the front of Car y from the rear of Car x.
    #3 x: Print the car numbers of the cars belonging to the connected component containing Car x, from front to back. 
    #x ≠ y
    #just before this query, no train is connected to the rear of Car x;
    #just before this query, no train is connected to the front of Car y;
    #just before this query, Car x and Car y belong to different connected components.
    #x ≠ y;
    #just before this query, the front of Car y is directly connected to the rear of Car x.  
    #3 x: Print the car numbers of the cars belonging to the connected component containing Car x, from front to back. 
    #1 ≦ x ≦ N
    #1 ≦ y ≦ N
    #All values in input are integers.
    #All queries satisfy the conditions in the Problem Statement.
    #The queries of the format 3 x ask to print at most 10^6 car numbers in total.
    #N ≦ 10^5
    #1 ≦ Q ≦ 10^5
    #input is given from Standard Input in the following format:
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
    #If a query with c_i = 3 asks to print the values j_1, j_2, ..., j_M, output the following line:
    #M j_

if __name__ == '__main__':
    main()