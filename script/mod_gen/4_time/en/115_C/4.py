def   main (): 
     N ,   K   =   map ( int ,   input (). split ()) 
     h   =   sorted ([ int ( input ())   for   _   in   range ( N )]) 
     ans   =   float ( 'inf' ) 
     for   i   in   range ( N   -   K   +   1 ): 
         ans   =   min ( ans ,   h [ i   +   K   -   1 ]   -   h [ i ]) 
     print ( ans )
