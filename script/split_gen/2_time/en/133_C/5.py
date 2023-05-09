def   main (): 
     L ,   R   =   map ( int ,   input (). split ()) 
     mod   =   2019 
     ans   =   mod 
     for   i   in   range ( L ,   min ( L   +   mod ,   R   +   1 )): 
         for   j   in   range ( i   +   1 ,   min ( i   +   mod ,   R   +   1 )): 
             ans   =   min ( ans ,   i   *   j   %   mod ) 
     print ( ans )
