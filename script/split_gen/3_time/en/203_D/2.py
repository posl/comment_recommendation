def   main ( ) : 
     N ,   K   =   map ( int ,   input ( ) . split ( ) ) 
     A   =   [ list ( map ( int ,   input ( ) . split ( ) ) )   for   _   in   range ( N ) ] 
     B   =   [ [ 0 ]   *   ( N + 1 )   for   _   in   range ( N + 1 ) ] 
     for   i   in   range ( N ) : 
         for   j   in   range ( N ) : 
             B [ i + 1 ] [ j + 1 ]   =   A [ i ] [ j ]   +   B [ i ] [ j + 1 ]   +   B [ i + 1 ] [ j ]   -   B [ i ] [ j ] 
     def   check ( x ) : 
         for   i   in   range ( N - K + 1 ) : 
             for   j   in   range ( N - K + 1 ) : 
                 if   B [ i + K ] [ j + K ]   +   B [ i ] [ j ]   -   B [ i + K ] [ j ]   -   B [ i ] [ j + K ]   <   K * K * x : 
                     return   True 
         return   False 
     ok   =   10 ** 9 
     ng   =   0 
     while   ok   -   ng   >   1 : 
         mid   =   ( ok   +   ng )   //   2 
         if   check ( mid ) : 
             ok   =   mid 
         else : 
             ng   =   mid 
     print ( ok )
