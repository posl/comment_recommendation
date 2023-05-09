def  main ( ) :
    # read the number of students and the number of queries
     n ,  q  =  map ( int ,  input ( ) . split ( ) )
    # read the heights of students
     a  =  list ( map ( int ,  input ( ) . split ( ) ) )
    # read the queries
     x  = [ int ( input ( ) )  for  _  in  range ( q ) ]
    # sort the heights in ascending order
     a . sort ( )
    # find the index of the first student with a height of at least x_j
     # by using binary search
     for  j  in  range ( q ) :
        print ( bisect . bisect_left ( a ,  x [ j ] ) )
