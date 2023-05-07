def   main (): 
     h ,   w ,   r_s ,   c_s   =   map ( int ,   input (). split ()) 
     n   =   int ( input ()) 
     r_c   =   [ tuple ( map ( int ,   input (). split ()))   for   _   in   range ( n )] 
     q   =   int ( input ()) 
     d_l   =   [ tuple ( input (). split ())   for   _   in   range ( q )] 
     r_c . sort () 
     for   r ,   c   in   r_c : 
         if   r   <   r_s   and   c   <   c_s : 
             r_s   -=   1 
         elif   r   <   r_s   and   c_s   <   c : 
             r_s   -=   1 
             c_s   +=   1 
         elif   r_s   <   r   and   c   <   c_s : 
             r_s   +=   1 
             c_s   -=   1 
         elif   r_s   <   r   and   c_s   <   c : 
             r_s   +=   1 
         elif   r   ==   r_s   and   c   <   c_s : 
             c_s   -=   1 
         elif   r   ==   r_s   and   c_s   <   c : 
             c_s   +=   1 
         elif   r   <   r_s   and   c   ==   c_s : 
             r_s   -=   1 
         elif   r_s   <   r   and   c   ==   c_s : 
             r_s   +=   1 
     for   d ,   l   in   d_l : 
         if   d   ==   'L' : 
             c_s   =   max ( c_s   -   l ,   1 ) 
         elif   d   ==   'R' : 
             c_s   =   min ( c_s   +   l ,   w ) 
         elif   d   ==   'U' : 
             r_s   =   max ( r_s   -   l ,   1 ) 
         elif   d   ==   'D' :
