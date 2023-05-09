def  lunlun( n ):
    q = [ 1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ,  9 ]
    for  i  in  range( n -  1 ):
        x = q.pop( 0 )
        d = x %  10 
        if  d >  0 :
            q.append( 10 * x + d -  1 )
        q.append( 10 * x + d )
        if  d <  9 :
            q.append( 10 * x + d +  1 )
     return  x
