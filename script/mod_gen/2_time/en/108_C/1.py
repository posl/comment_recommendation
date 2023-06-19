def   main (): 
     n ,   k   =   map ( int ,   input (). split ()) 
     ans   =   0 
     for   a   in   range ( 1 ,   n   +   1 ): 
         if   a   %   k   ==   0 : 
             ans   +=   1   *   n   **   2 
         elif   a   %   k   ==   k   //   2 : 
             ans   +=   3   *   ( n   //   k   +   1 )   *   ( n   //   k )   +   1   *   ( n   %   k   >=   k   //   2 ) 
         else : 
             ans   +=   3   *   ( n   //   k   +   1 )   *   ( n   //   k   +   1 ) 
     print ( ans )
