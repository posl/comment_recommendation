def   main (): 
     N   =   int ( input ()) 
     A   =   list ( map ( int ,   input (). split ())) 
     MOD   =   998244353 
     ans   =   [ 0 ] * 10 
     for   i   in   range ( 10 ): 
         cnt   =   0 
         for   a   in   A : 
             cnt   +=   ( a   ==   i ) 
         ans [ i ]   +=   cnt 
     for   i   in   range ( N   -   1 ): 
         nxt   =   [ 0 ] * 10 
         for   j   in   range ( 10 ): 
             for   k   in   range ( 10 ): 
                 if   ( j   +   k )   %   10   ==   A [ i + 1 ]: 
                     nxt [ j ]   +=   ans [ k ] 
                 if   ( j   *   k )   %   10   ==   A [ i + 1 ]: 
                     nxt [ j ]   +=   ans [ k ] 
         ans   =   nxt 
     for   i   in   range ( 10 ): 
         print ( ans [ i ]   %   MOD )

if __name__ == '__main__':
    ()