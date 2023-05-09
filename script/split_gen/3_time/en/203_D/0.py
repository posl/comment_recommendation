def   main (): 
     N ,   K   =   map ( int ,   input (). split ()) 
     A   =   [ list ( map ( int ,   input (). split ()))   for   _   in   range ( N )] 
     A   =   [ [ 0 ]   +   a   +   [ 0 ]   for   a   in   A ] 
     A . insert ( 0 ,   [ 0 ]   *   ( N   +   2 )) 
     A . append ( [ 0 ]   *   ( N   +   2 )) 
     for   i   in   range ( N ): 
         for   j   in   range ( N ): 
             A [ i   +   1 ][ j   +   1 ]   +=   A [ i   +   1 ][ j ]   +   A [ i ][ j   +   1 ]   -   A [ i ][ j ] 
     def   check ( x ): 
         for   i   in   range ( N   -   K   +   1 ): 
             for   j   in   range ( N   -   K   +   1 ): 
                 if   A [ i   +   K ][ j   +   K ]   -   A [ i   +   K ][ j ]   -   A [ i ][ j   +   K ]   +   A [ i ][ j ]   <   K   *   K   *   x : 
                     return   True 
         return   False 
     left   =   0 
     right   =   10 ** 9 
     while   right   -   left   >   1 : 
         mid   =   ( left   +   right )   //   2 
         if   check ( mid ): 
             right   =   mid 
         else : 
             left   =   mid 
     print ( right )
