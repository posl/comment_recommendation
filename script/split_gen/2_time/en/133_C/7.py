def   main () : 
     L ,  R   =   map ( int ,  input (). split ()) 
     # 2019 is the smallest prime number that is greater than or equal to 2019. 
     if   R   -   L   >=   2019 : 
         print ( 0 ) 
         return 
     # We can easily find the minimum value of (i × j)  mod  2019 
     # by considering all the possible pairs of (i, j). 
     min_mod   =   2019 
     for   i   in   range ( L ,  R ): 
         for   j   in   range ( i   +   1 ,  R   +   1 ): 
             min_mod   =   min ( min_mod ,   ( i   *   j )   %   2019 ) 
     print ( min_mod )
