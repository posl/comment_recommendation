def   main (): 
     N   =   int ( input ()) 
     A   =   list ( map ( int ,   input (). split ())) 
     M   =   200 
     dp   =   [ None   for   i   in   range ( M )] 
     dp [ A [ 0 ]   %   M ]   =   [ 0 ] 
     for   i   in   range ( 1 ,   N ): 
         if   dp [ A [ i ]   %   M ]   is   None : 
             dp [ A [ i ]   %   M ]   =   [ i ] 
         else : 
             print ( "Yes" ) 
             print ( len ( dp [ A [ i ]   %   M ]),   " " . join ( map ( str ,   map ( lambda   x :   x   +   1 ,   dp [ A [ i ]   %   M ]))),   sep = "
" ) 
             print ( 1 ,   i   +   1 ,   sep = "
" ) 
             exit () 
         for   j   in   range ( M ): 
             if   dp [ j ]   is   None : 
                 continue 
             if   dp [( j   +   A [ i ])   %   M ]   is   None : 
                 dp [( j   +   A [ i ])   %   M ]   =   dp [ j ]   +   [ i ] 
             else : 
                 print ( "Yes" ) 
                 print ( len ( dp [ j ]),   " " . join ( map ( str ,   map ( lambda   x :   x   +   1 ,   dp [ j ]))),   sep = "
" ) 
                 print ( len ( dp [( j   +   A [ i ])   %   M ]),   " " . join ( map ( str ,   map ( lambda   x :   x   +   1 ,   dp [( j   +   A [ i ])   %   M ]))),   sep = "
" ) 
                 exit () 
     print ( "No" )

if __name__ == '__main__':
    ()