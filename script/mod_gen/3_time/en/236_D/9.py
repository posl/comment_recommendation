def dfs ( i , j , k , l , m , n , o ) : if i == n : return 0 if j == 0 : return dfs ( i + 1 , 0 , 0 , 0 , 0 , n , o ) if j == 1 : return max ( dfs ( i , 0 , k , l , m , n , o ) , dfs ( i , 0 , k , l , m , n , o ) ^ o [ i ][ k ]) if j == 2 : return max ( dfs ( i , 1 , k , l , m , n , o ) , dfs ( i , 1 , k , l , m , n , o ) ^ o [ i ][ l ]) if j == 3 : return max ( dfs ( i , 2 , k , l , m , n , o ) , dfs ( i , 2 , k , l , m , n , o ) ^ o [ i ][ m ]) if j == 4 : return max ( dfs ( i , 3 , k , l , m , n , o ) , dfs ( i , 3 , k , l , m , n , o ) ^ o [ i ][ k ], dfs ( i , 3 , k , l , m , n , o ) ^ o [ i ][ l ], dfs ( i , 3 , k , l , m , n , o ) ^ o [ i ][ m ])
n = int ( input ()) o = [ list ( map ( int , input (). split ())) for i in range ( n )] print ( dfs ( 0 , 0 , 0 , 0 , 0 , n , o ))
I was able to solve this problem using the following code. It is not the most efficient code, but it is easy to understand. I used the following strategy.
I used the following strategy.
I used the following strategy.
I used the following strategy.
I used the f

if __name__ == '__main__':
    dfs()