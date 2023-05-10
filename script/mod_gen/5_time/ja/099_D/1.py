def get_minimum_change_cost( N, C, D, G ):
    # 2次元配列の初期化
    dp = [ [ 0 for i in range( C ) ] for j in range( N ) ]
    # dp[ i ][ j ] = i列目まで塗り替えて、i列目をj色にしたときの、最小の塗り替えコスト
    # dp[ i ][ j ] = min( dp[ i - 1 ][ k ] ) + D[ k ][ j ] ( k = 0, 1, ..., C - 1 )
    # 初期化
    for i in range( C ):
        dp[ 0 ][ i ] = D[ i ][ G[ 0 ] - 1 ]
    # DP
    for i in range( 1, N ):
        for j in range( C ):
            dp[ i ][ j ] = min( [ dp[ i - 1 ][ k ] for k in range( C ) if k != j ] ) + D[ j ][ G[ i ] - 1 ]
    # 答えは、最後の列の最小値
    return min( dp[ -1 ] )

if __name__ == '__main__':
    get_minimum_change_cost()