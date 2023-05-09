def   main (): 
     n   =   int ( input ()) 
     v   =   list ( map ( int ,   input (). split ())) 
     v1   =   v [:: 2 ] 
     v2   =   v [ 1 :: 2 ] 
     c1   =   Counter ( v1 ) 
     c2   =   Counter ( v2 ) 
     m1 ,   m2   =   c1 . most_common ( 1 )[ 0 ][ 0 ],   c2 . most_common ( 1 )[ 0 ][ 0 ] 
     if   m1   !=   m2 : 
         print ( n   -   c1 [ m1 ]   -   c2 [ m2 ]) 
     else : 
         m1 ,   m2   =   c1 . most_common ( 2 )[ 1 ][ 0 ],   c2 . most_common ( 2 )[ 1 ][ 0 ] 
         print ( min ( n   -   c1 [ m1 ]   -   c2 [ m2 ],   n   -   c1 [ m2 ]   -   c2 [ m1 ]))
