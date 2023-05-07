def   main (): 
     N   =   int ( input ()) 
     A   =   [] 
     for   i   in   range ( N ): 
         A . append ( int ( input ())) 
         for   j   in   range ( A [ i ]): 
             x ,   y   =   map ( int ,   input (). split ()) 
     # print(N) 
     # print(A) 
     # print(x) 
     # print(y) 
     ans   =   0 
     for   i   in   range ( 2 ** N ): 
         # print(i) 
         honest   =   [ False ]   *   N 
         for   j   in   range ( N ): 
             if   ( i   >>   j )   &   1 : 
                 honest [ j ]   =   True 
         # print(honest) 
         flag   =   True 
         for   j   in   range ( N ): 
             if   honest [ j ]: 
                 for   k   in   range ( A [ j ]): 
                     x ,   y   =   map ( int ,   input (). split ()) 
                     if   y   ==   1   and   honest [ x - 1 ]   ==   False : 
                         flag   =   False 
                     if   y   ==   0   and   honest [ x - 1 ]: 
                         flag   =   False 
         if   flag : 
             ans   =   max ( ans ,   honest . count ( True )) 
     print ( ans )
