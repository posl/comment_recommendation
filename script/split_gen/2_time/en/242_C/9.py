def   main (): 
     N   =   int ( input ()) 
     # dp[i][j][k] := i桁目まで見て、jで終わり、k=0のとき、i桁目とi+1桁目の差が1以下
     dp   =   [[[ 0   for   _   in   range ( 2 )]   for   _   in   range ( 10 )]   for   _   in   range ( N +  1 )] 
     for   i   in   range ( 1 ,   10 ): 
         dp [ 1 ][ i ][ 0 ]   =   1 
         dp [ 1 ][ i ][ 1 ]   =   1 
     for   i   in   range ( 2 ,   N +  1 ): 
         for   j   in   range ( 10 ): 
             if   j   ==   0 : 
                 dp [ i ][ j ][ 0 ]   =   dp [ i -  1 ][ j +  1 ][ 0 ] 
                 dp [ i ][ j ][ 1 ]   =   dp [ i -  1 ][ j +  1 ][ 0 ]   +   dp [ i -  1 ][ j +  1 ][ 1 ] 
             elif   j   ==   9 : 
                 dp [ i ][ j ][ 0 ]   =   dp [ i -  1 ][ j -  1 ][ 0 ] 
                 dp [ i ][ j ][ 1 ]   =   dp [ i -  1 ][ j -  1 ][ 0 ]   +   dp [ i -  1 ][ j -  1 ][ 1 ] 
             else : 
                 dp [ i ][ j ][ 0 ]   =   dp [ i -  1 ][ j -  1 ][ 0 ]   +   dp [ i -  1 ][ j +  1 ][ 0 ] 
                 dp [ i ][ j ][ 1 ]   =   dp [ i -  1 ][ j -  1 ][ 0 ]   +   dp [ i -  1 ][ j -  1 ][ 1 ]   +   dp [ i -
