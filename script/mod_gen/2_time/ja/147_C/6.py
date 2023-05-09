def   main ():
     N   =   int ( input ())
     A   =   [ 0   for   _   in   range ( N )]
     X   =   [ []   for   _   in   range ( N )]
     Y   =   [ []   for   _   in   range ( N )]
     for   i   in   range ( N ):
         A [ i ]   =   int ( input ())
         for   j   in   range ( A [ i ]):
             x ,   y   =   map ( int ,   input (). split ())
             X [ i ]. append ( x - 1 )
             Y [ i ]. append ( y )
     ans   =   0 
     for   bit   in   range ( 2 ** N ):
         ok   =   True 
         for   i   in   range ( N ):
             if   ( bit   >>   i )   &   1 :
                 for   j   in   range ( A [ i ]):
                     if   Y [ i ][ j ]   ==   1 :
                         if   not   ( bit   >>   X [ i ][ j ])   &   1 :
                             ok   =   False 
                     else :
                         if   ( bit   >>   X [ i ][ j ])   &   1 :
                             ok   =   False 
         if   ok :
             ans   =   max ( ans ,   bin ( bit ). count ( "1" ))
     print ( ans )

if __name__ == '__main__':
    ()