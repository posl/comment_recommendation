def   main ():
     N ,  K   =   map ( int ,  input (). split ())
     L ,  R   =   [],   []
     for   _   in   range ( K ):
         l ,  r   =   map ( int ,  input (). split ())
         L . append ( l )
         R . append ( r )
     # dp[i] = number of ways to reach Cell i
     dp   =   [ 0 ] * ( N + 1 )
     dp [ 0 ]   =   1 
     # sum_dp[i] = sum of dp[0] + dp[1] + ... + dp[i]
     sum_dp   =   [ 0 ] * ( N + 1 )
     sum_dp [ 0 ]   =   1 
     for   i   in   range ( N ):
         for   j   in   range ( K ):
             dp [ i + L [ j ]]   +=   sum_dp [ i ] - sum_dp [ max ( 0 ,  i - R [ j ])] 
             dp [ i + L [ j ]]   %=   998244353 
         sum_dp [ i + 1 ]   =   ( sum_dp [ i ] + dp [ i + 1 ]) %  998244353 
     print ( dp [ N ])
