def   main ():
    n   =   int ( input ())
    sx , sy , tx , ty   =   map ( int , input (). split ())
    x , y , r   =   [ []   for   _   in   range ( 3 )], [ []   for   _   in   range ( 3 )], [ []   for   _   in   range ( 3 )]
     for   i   in   range ( n ):
        x [ i ], y [ i ], r [ i ]   =   map ( int , input (). split ())
    ans   =   0 
     if   n   ==   1 :
        d   =   (( x [ 0 ] - sx ) ** 2   +   ( y [ 0 ] - sy ) ** 2 ) ** 0.5   +   (( x [ 0 ] - tx ) ** 2   +   ( y [ 0 ] - ty ) ** 2 ) ** 0.5 
         if   d   <=   r [ 0 ]:
            ans   =   1 
     elif   n   ==   2 :
        d1   =   (( x [ 0 ] - sx ) ** 2   +   ( y [ 0 ] - sy ) ** 2 ) ** 0.5   +   (( x [ 0 ] - tx ) ** 2   +   ( y [ 0 ] - ty ) ** 2 ) ** 0.5 
        d2   =   (( x [ 1 ] - sx ) ** 2   +   ( y [ 1 ] - sy ) ** 2 ) ** 0.5   +   (( x [ 1 ] - tx ) ** 2   +   ( y [ 1 ] - ty ) ** 2 ) ** 0.5 
        d3   =   (( x [ 0 ] - sx ) ** 2   +   ( y [ 0 ] - sy ) ** 2 ) ** 0.5   +   (( x [ 1 ] - tx ) ** 2   +   ( y [ 1 ] - ty ) ** 2 ) ** 0.5 
        d4   =   (( x [ 1 ] - sx ) ** 2   +   ( y [ 1 ] -

if __name__ == '__main__':
    ()