def   main (): 
     N ,  K   =   map ( int ,  input (). split ()) 
     h   =   sorted ( list ( map ( int ,  input (). split ()))) 
     ans   =   10 ** 9 
     for   i   in   range ( N   -  K   +   1 ): 
         ans   =   min ( ans ,  h [ i   +  K   -   1 ]   -  h [ i ]) 
     print ( ans )
