def   main (): 
     # Input 
     N ,   K   =   map ( int ,   input (). split ()) 
     H   =   sorted ( map ( int ,   input () for _   in   range ( N ))) 
     # Solve 
     ans   =   float ( 'inf' ) 
     for   i   in   range ( N   -   K   +   1 ): 
         ans   =   min ( ans ,   H [ i   +   K   -   1 ]   -   H [ i ]) 
     # Output 
     print ( ans )

if __name__ == '__main__':
    ()