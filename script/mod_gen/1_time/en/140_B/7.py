def   main (): 
     # input 
     N   =   int ( input ()) 
     A   =   list ( map ( int ,   input (). split ())) 
     B   =   list ( map ( int ,   input (). split ())) 
     C   =   list ( map ( int ,   input (). split ())) 
     # initialize 
     ans   =   0 
     # count 
     for   i   in   range ( N ): 
         ans   +=   B [ A [ i ]   -   1 ] 
         if   i   !=   0   and   A [ i ]   -   A [ i   -   1 ]   ==   1 : 
             ans   +=   C [ A [ i   -   1 ]   -   1 ] 
     # output 
     print ( ans )

if __name__ == '__main__':
    ()