def   main (): 
     N ,   K   =   map ( int ,   input (). split ()) 
     A   =   [ list ( map ( int ,   input (). split ()))   for   _   in   range ( N )] 
     def   check ( x ): 
         B   =   [ [ 0   for   _   in   range ( N + 1 )]   for   _   in   range ( N + 1 )] 
         for   i   in   range ( N ): 
             for   j   in   range ( N ): 
                 B [ i + 1 ][ j + 1 ]   =   B [ i + 1 ][ j ]   +   B [ i ][ j + 1 ]   -   B [ i ][ j ]   +   ( A [ i ][ j ]   <   x ) 
         for   i   in   range ( K ,   N + 1 ): 
             for   j   in   range ( K ,   N + 1 ): 
                 if   B [ i ][ j ]   -   B [ i - K ][ j ]   -   B [ i ][ j - K ]   +   B [ i - K ][ j - K ]   <   K * K   //   2   +   1 : 
                     return   True 
         return   False 
     ok   =   0 
     ng   =   10 ** 9   +   1 
     while   ng   -   ok   >   1 : 
         mid   =   ( ok   +   ng )   //   2 
         if   check ( mid ): 
             ok   =   mid 
         else : 
             ng   =   mid 
     print ( ok )

if __name__ == '__main__':
    ()