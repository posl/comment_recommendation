def   main (): 
     N   =   int ( input ()) 
     G   =   [[]   for   _   in   range ( N + 1 )] 
     for   _   in   range ( N - 1 ): 
         a ,   b   =   map ( int ,   input (). split ()) 
         G [ a ]. append ( b ) 
         G [ b ]. append ( a ) 
     # 頂点の番号を 1 から N にするために -1 する 
     # 0 はダミー 
     color   =   [ 0 ]   *   ( N + 1 ) 
     # 木なので 1 から探索すればよい 
     dfs ( G ,   1 ,   color ) 
     print ( max ( color )) 
     for   i   in   range ( 2 ,   N + 1 ): 
         print ( color [ i ])
