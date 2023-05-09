def   main (): 
     L ,  R   =   map ( int ,   input (). split ()) 
     ans   =   2018 
     for   i   in   range ( L ,  R   +   1 ): 
         for   j   in   range ( i   +   1 ,  R   +   1 ): 
             ans   =   min ( ans ,   i   *   j   %   2019 ) 
             if   ans   ==   0 : 
                 break 
         else : 
             continue 
         break 
     print ( ans )
