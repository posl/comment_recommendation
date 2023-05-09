def   main () : 
     #input 
     N   =   int ( input ()) 
     S   =   [] 
     for   i   in   range ( N ): 
         S . append ( input ()) 
     #solve 
     d   =   {} 
     for   s   in   S : 
         if   s   in   d : 
             d [ s ]   +=   1 
         else : 
             d [ s ]   =   1 
     max_votes   =   max ( d . values ()) 
     for   k ,   v   in   d . items (): 
         if   v   ==   max_votes : 
             print ( k )
