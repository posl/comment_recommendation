def dp ( n , k , l , r ): # n: N, k: K, l: L_i, r: R_i dp = [ 0 for _ in range ( n )] dp [ 0 ] = 1 for i in range ( n - 1 ): for j in range ( k ): dp [ i + l [ j ]] += dp [ i ] dp [ i + l [ j ]] %= 998244353 for j in range ( k ): dp [ i + r [ j ] + 1 ] -= dp [ i ] dp [ i + r [ j ] + 1 ] %= 998244353 return dp [ n - 1 ] n , k = map ( int , input (). split ()) l = [ 0 ] * k r = [ 0 ] * k for i in range ( k ): l [ i ], r [ i ] = map ( int , input (). split ()) print ( dp ( n , k , l , r ))

if __name__ == '__main__':
    dp()