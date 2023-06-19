def   main (): 
     import   sys 
     import   heapq 
     input   =   sys . stdin . readline 
     Q   =   int ( input ()) 
     heap   =   [] 
     sum   =   0 
     for   _   in   range ( Q ): 
         p ,   x   =   map ( int ,   input (). split ()) 
         if   p   ==   1 : 
             heapq . heappush ( heap ,   x   -   sum ) 
         elif   p   ==   2 : 
             sum   +=   x 
         else : 
             print ( heapq . heappop ( heap )   +   sum )
