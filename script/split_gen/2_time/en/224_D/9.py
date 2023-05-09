def find_empty_vertex ( graph ) : 
     for   i   in   range ( 9 ) : 
         if   i   not   in   graph : 
             return   i 
 def   find_adjacent_vertices ( graph ,   vertex ) : 
     return   [ v   for   v   in   graph [ vertex ]   if   v   in   graph ] 
 def   find_adjacent_pieces ( graph ,   pieces ,   vertex ) : 
     return   [ pieces [ v ]   for   v   in   graph [ vertex ]   if   v   in   graph ] 
 def   find_piece ( pieces ,   vertex ) : 
     return   pieces . index ( vertex ) 
 def   find_empty_piece ( pieces ) : 
     return   pieces . index ( - 1 ) 
 def   is_complete ( pieces ) : 
     return   all ( [ pieces [ i ]   ==   i   for   i   in   range ( 8 ) ] ) 
 def   solve ( graph ,   pieces ,   num_operations ) : 
     if   is_complete ( pieces ) : 
         return   num_operations 
     empty_vertex   =   find_empty_vertex ( graph ) 
     adjacent_vertices   =   find_adjacent_vertices ( graph ,   empty_vertex ) 
     adjacent_pieces   =   find_adjacent_pieces ( graph ,   pieces ,   empty_vertex ) 
     empty_piece   =   find_empty_piece ( pieces ) 
     for   ( vertex ,   piece )   in   zip ( adjacent_vertices ,   adjacent_pieces ) : 
         pieces [ empty_piece ]   =   vertex 
         pieces [ piece ]   =   - 1 
         del   graph [ empty_vertex ] 
         graph [ vertex ]   =   [ edge   for   edge   in   graph [ vertex ]   if   edge   !=   empty_vertex ] 
         num_operations   +=   1 
         ret   =   solve ( graph ,   pieces ,   num_operations ) 
         if   ret   !=   - 1 : 
             return   ret 
         pieces [ empty_piece ]   =   - 1 
         pieces [ piece ]   =   vertex 
         graph [ vertex ]   =   adjacent_vertices 
         graph [ empty_vertex ]   =   [ edge   for   edge   in   graph [ empty_vertex ]   if   edge   !=   vertex ]
