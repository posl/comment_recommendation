def   count_ways ( n ,  k ,  l ,  r ): 
     # dp[i] is the number of ways to reach cell i 
     dp   =   [ 0 ]   *   ( n   +   1 ) 
     dp [ 0 ]   =   1 
     for   i   in   range ( n ): 
         for   j   in   range ( k ): 
             if   i   +   l [ j ]   <=   n : 
                 dp [ i   +   l [ j ]]   +=   dp [ i ] 
             if   i   +   r [ j ]   +   1   <=   n : 
                 dp [ i   +   r [ j ]   +   1 ]   -=   dp [ i ] 
         dp [ i   +   1 ]   +=   dp [ i ] 
     return   dp [ n ]

if __name__ == '__main__':
    ()