def   solve ( N ,   X ,   A ): 
     # dp[i][j] = the number of ways to choose the first i bags 
     # so that the product of the numbers written on the chosen balls is j 
     dp   =   [ [ 0 ]   *   ( X   +   1 )   for   _   in   range ( N   +   1 )] 
     dp [ 0 ][ 1 ]   =   1 
     for   i   in   range ( N ): 
         for   j   in   range ( X   +   1 ): 
             for   k   in   range ( 1 ,   A [ i ][ 0 ]   +   1 ): 
                 if   j   *   A [ i ][ k ]   <=   X : 
                     dp [ i   +   1 ][ j   *   A [ i ][ k ]]   +=   dp [ i ][ j ] 
     return   dp [ N ][ X ]
