def dfs ( v , p , d , edges , ans ): for e in edges [ v ]: if e [ 0 ] == p : continue ans [ e [ 0 ]] = v dfs ( e [ 0 ], v , d + 1 , edges , ans )

if __name__ == '__main__':
    dfs()