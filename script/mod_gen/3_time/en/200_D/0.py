def   main (): 
     N   =   int ( input ()) 
     A   =   list ( map ( int ,   input (). split ())) 
     A   =   [ a   %   200   for   a   in   A ] 
     dp   =   [ 0   for   _   in   range ( 200 )] 
     for   i   in   range ( N ): 
         dp2   =   [ 0   for   _   in   range ( 200 )] 
         for   j   in   range ( 200 ): 
             dp2 [( j   +   A [ i ])   %   200 ]   =   dp [ j ] 
             dp2 [ j ]   =   max ( dp2 [ j ],   dp [ j ]) 
         dp2 [ A [ i ]]   =   max ( dp2 [ A [ i ]],   1 ) 
         dp   =   dp2 
     if   max ( dp )   <   2 : 
         print ( 'No' ) 
     else : 
         print ( 'Yes' ) 
         x   =   dp . index ( 1 ) 
         y   =   dp . index ( 2 ) 
         B   =   [] 
         C   =   [] 
         for   i   in   range ( N ): 
             if   A [ i ]   ==   x : 
                 B . append ( i   +   1 ) 
             elif   A [ i ]   ==   y : 
                 C . append ( i   +   1 ) 
         print ( len ( B ),   ' ' . join ( map ( str ,   B ))) 
         print ( len ( C ),   ' ' . join ( map ( str ,   C )))

if __name__ == '__main__':
    ()