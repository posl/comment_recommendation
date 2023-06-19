def   main (): 
     N ,   X ,   Y   =   map ( int ,   input (). split ()) 
     graph   =   [ []   for   i   in   range ( N )] 
     for   i   in   range ( N - 1 ): 
         graph [ i ]. append ( i + 1 ) 
         graph [ i + 1 ]. append ( i ) 
     graph [ X - 1 ]. append ( Y - 1 ) 
     graph [ Y - 1 ]. append ( X - 1 ) 
     ans   =   [ 0   for   i   in   range ( N - 1 )] 
     for   i   in   range ( N ): 
         dist   =   [ - 1   for   j   in   range ( N )] 
         dist [ i ]   =   0 
         que   =   [ i ] 
         while   que : 
             v   =   que . pop ( 0 ) 
             for   j   in   graph [ v ]: 
                 if   dist [ j ]   ==   - 1 : 
                     dist [ j ]   =   dist [ v ]   +   1 
                     que . append ( j ) 
         for   j   in   range ( i + 1 ,   N ): 
             ans [ dist [ j ] - 1 ]   +=   1 
     for   i   in   range ( N - 1 ): 
         print ( ans [ i ])
