def   f ( x ): 
     if   x   <=   9 : 
         return   x 
     d   =   len ( str ( x )) 
     return   ( 10   **   ( d   -   1 )   -   1 )   +   9   *   ( d   -   1 )   +   f ( x   -   10   **   ( d   -   1 )   +   1 )
