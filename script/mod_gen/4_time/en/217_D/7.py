def main():
    L, Q = map(int, input().split())
    #L: length of timber
    #Q: number of queries
    #c_i: 1 or 2 (1 <= i <= Q)
    #x_i: 1 <= x_i <= L - 1 (1 <= i <= Q)
    #for c_i = 1, 2, it is guaranteed that there will have been no cut at Mark x_i when the query is to be processed.
    #All values in input are integers.
    #At the time of the first query, no cut has been made, so the piece with Mark 2 has a length of 5 meters. Thus, you should print 5.
    #In the second query, the piece is cut into two pieces with lengths of 3 and 2 meters.
    #At the time of the third query, the piece with Mark 2 has a length of 3 meters, so you should print 3.  
    #In the j-th line, print the response to the j-th such query.
    #L: length of timber
    #Q: number of queries
    #c_i: 1 or 2 (1 <= i <= Q)
    #x_i: 1 <= x_i <= L - 1 (1 <= i <= Q)
    #for c_i = 1, 2, it is guaranteed that there will have been no cut at Mark x_i when the query is to be processed.
    #All values in input are integers.
    #At the time of the first query, no cut has been made, so the piece with Mark 2 has a length of 5 meters. Thus, you should print 5.
    #In the second query, the piece is cut into two pieces with lengths of 3 and 2 meters.
    #At the time of the third query, the piece with Mark 2 has a length of 3 meters, so you should print 3.  
    #In the j-th line, print the response to the j-th such query.
    #print(L, Q)
    #print("c_i, x_i")
    #for i in range(Q):
    #    c_i, x_i = map(int, input().split())
    #    print(c_i, x_i)
    #print(L, Q)
    #print("c_i

if __name__ == '__main__':
    main()