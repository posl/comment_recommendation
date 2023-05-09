def   main (): 
     n ,   m ,   q   =   map ( int ,   input (). split ()) 
     a ,   b ,   c ,   d   =   [],   [],   [],   [] 
     for   _   in   range ( q ): 
         _a ,   _b ,   _c ,   _d   =   map ( int ,   input (). split ()) 
         a . append ( _a ) 
         b . append ( _b ) 
         c . append ( _c ) 
         d . append ( _d ) 
     ans   =   0 
     for   i   in   range ( 1 ,   m   +   1 ): 
         ans   =   max ( ans ,   dfs ([ i ],   n ,   m ,   q ,   a ,   b ,   c ,   d )) 
     print ( ans )
