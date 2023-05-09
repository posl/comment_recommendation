def   main (): 
     n   =   int ( input ()) 
     p   =   list ( map ( int ,   input (). split ())) 
     q   =   list ( map ( int ,   input (). split ())) 
     fact   =   [ 1 ] 
     for   i   in   range ( 1 ,   n + 1 ): 
         fact . append ( fact [ i - 1 ]   *   i ) 
     def   lex ( l ): 
         ans   =   0 
         for   i   in   range ( n ): 
             ans   +=   ( l [ i ]   -   1 )   *   fact [ n - 1 - i ] 
             for   j   in   range ( i + 1 ,   n ): 
                 if   l [ j ]   >   l [ i ]: 
                     l [ j ]   -=   1 
         return   ans 
     print ( abs ( lex ( p )   -   lex ( q )))

if __name__ == '__main__':
    ()