def   main (): 
     N   =   int ( input ()) 
     A   =   list ( map ( int ,   input (). split ())) 
     MOD   =   998244353 
     ans   =   [ 0 ] * 10 
     for   i   in   range ( 10 ): 
         cnt   =   0 
         for   j   in   range ( N ): 
             if   A [ j ]   ==   i : 
                 cnt   +=   1 
         ans [ i ]   =   pow ( 2 ,   cnt ,   MOD )   -   1 
     print ( "
" . join ( map ( str ,   ans )))
