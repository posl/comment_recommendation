def   main ():
     n   =   int ( input ())
     a   =   list ( map ( int ,   input (). split ()))
     b   =   [ 0 ]* n
     c   =   [ 0 ]* n
     for   i   in   range ( n ):
         b [ i ]   =   [ a [ i ],   i ]
     b . sort ()
     for   i   in   range ( n ):
         c [ b [ i ][ 1 ]]   =   i 
     d   =   [ 0 ]* n 
     for   i   in   range ( n ):
         d [ c [ i ]]   +=   1 
     e   =   [ 0 ]* n 
     for   i   in   range ( n ):
         e [ i ]   =   e [ i - 1 ]   +   d [ i ]
     f   =   [ 0 ]* n 
     for   i   in   range ( n ):
         f [ i ]   =   e [ i ]   -   e [ c [ i ]]
     for   i   in   range ( n ):
         print ( f [ i ])
