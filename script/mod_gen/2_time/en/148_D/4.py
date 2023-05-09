def   main (): 
     N   =   int ( input ()) 
     a   =   list ( map ( int ,   input (). split ())) 
     ans   =   0 
     for   i   in   range ( N ): 
         if   a [ i ]   ==   i   +   1 : 
             ans   +=   1 
             a [ i ]   =   0 
     if   ans   ==   N : 
         print ( - 1 ) 
     else : 
         print ( N   -   ans )

if __name__ == '__main__':
    ()