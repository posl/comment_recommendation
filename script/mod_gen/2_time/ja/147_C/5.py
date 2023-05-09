def   main (): 
     N   =   int ( input ()) 
     A   =   [] 
     for   i   in   range ( N ): 
         A_i   =   int ( input ()) 
         A_i_list   =   [] 
         for   j   in   range ( A_i ): 
             x ,   y   =   map ( int ,   input (). split ()) 
             A_i_list . append (( x ,   y )) 
         A . append ( A_i_list ) 
     ans   =   0 
     for   i   in   range ( 2 ** N ): 
         honest   =   [ False   for   j   in   range ( N )] 
         for   j   in   range ( N ): 
             if   (( i   >>   j )   &   1 ): 
                 honest [ j ]   =   True 
         flag   =   True 
         for   j   in   range ( N ): 
             if   honest [ j ]: 
                 for   x ,   y   in   A [ j ]: 
                     if   y   ==   1 : 
                         if   not   honest [ x   -   1 ]: 
                             flag   =   False 
                     else : 
                         if   honest [ x   -   1 ]: 
                             flag   =   False 
         if   flag : 
             ans   =   max ( ans ,   honest . count ( True )) 
     print ( ans )

if __name__ == '__main__':
    ()