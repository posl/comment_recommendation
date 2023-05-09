def   main ():
    n, m, k   =   map ( int ,   input (). split ())
    mod   =   998244353
    dp   =   [ [ [ 0   for   _   in   range ( k + 1 )]   for   _   in   range ( m + 1 )]   for   _   in   range ( n + 1 )]
    dp [ 0 ][ 0 ][ 0 ]   =   1
    for   i   in   range ( n ):
         for   j   in   range ( m ):
             for   x   in   range ( k + 1 ):
                 dp [ i + 1 ][ j + 1 ][ x ]   +=   dp [ i ][ j ][ x ]
                 dp [ i + 1 ][ j + 1 ][ x ]   %=   mod
                 if   x   +   j   +   1   <=   k :
                     dp [ i + 1 ][ j + 1 ][ x   +   j   +   1 ]   +=   dp [ i ][ j ][ x ]
                     dp [ i + 1 ][ j + 1 ][ x   +   j   +   1 ]   %=   mod
    res   =   sum ( dp [ n ][ m ])   %   mod
     print ( res )

if __name__ == '__main__':
    ()