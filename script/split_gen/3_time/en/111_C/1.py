def   main (): 
     n   =   int ( input ()) 
     v   =   list ( map ( int ,   input (). split ())) 
     odd   =   v [:: 2 ] 
     even   =   v [ 1 :: 2 ] 
     odd1   =   max ( odd ,   key = odd . count ) 
     odd2   =   max ( odd ,   key = odd . count ,   default = None ) 
     even1   =   max ( even ,   key = even . count ) 
     even2   =   max ( even ,   key = even . count ,   default = None ) 
     if   odd1   !=   odd2   and   even1   !=   even2 : 
         print ( n   -   max ( odd . count ( odd1 ),   odd . count ( odd2 ),   even . count ( even1 ),   even . count ( even2 ))) 
     elif   odd1   ==   odd2   and   even1   ==   even2 : 
         print ( n   //   2 ) 
     elif   odd1   ==   odd2 : 
         print ( n   -   max ( odd . count ( odd1 ),   even . count ( even1 ),   even . count ( even2 ))) 
     else : 
         print ( n   -   max ( odd . count ( odd1 ),   odd . count ( odd2 ),   even . count ( even1 )))
