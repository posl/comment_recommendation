def   main (): 
     N ,   K   =   map ( int ,   input (). split ()) 
     LR   =   [ tuple ( map ( int ,   input (). split ()))   for   _   in   range ( K )] 
     MOD   =   998244353 
     dp   =   [ 0 ]   *   ( N + 1 ) 
     dp [ 0 ]   =   1 
     for   i   in   range ( N ): 
         for   l ,   r   in   LR : 
             dp [ min ( i + r ,   N )]   +=   dp [ max ( i + l ,   0 )] 
             dp [ min ( i + r ,   N )]   %=   MOD 
     print ( dp [ - 1 ])
