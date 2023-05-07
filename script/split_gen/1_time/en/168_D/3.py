def   main (): 
     N ,   M   =   map ( int ,   input (). split ()) 
     G   =   [[]   for   _   in   range ( N + 1 )] 
     for   _   in   range ( M ): 
         a ,   b   =   map ( int ,   input (). split ()) 
         G [ a ]. append ( b ) 
         G [ b ]. append ( a ) 
     dist   =   [- 1 ]   *   ( N + 1 ) 
     dist [ 1 ]   =   0 
     q   =   [ 1 ] 
     while   q : 
         v   =   q . pop () 
         for   nv   in   G [ v ]: 
             if   dist [ nv ]   !=   - 1 : 
                 continue 
             dist [ nv ]   =   dist [ v ]   +   1 
             q . append ( nv ) 
     if   - 1   in   dist [ 2 :]: 
         print ( "No" ) 
     else : 
         print ( "Yes" ) 
         for   i   in   range ( 2 ,   N + 1 ): 
             for   nv   in   G [ i ]: 
                 if   dist [ i ]   ==   dist [ nv ]   +   1 : 
                     print ( nv ) 
                     break
