def   f ( x ): 
     if   x   ==   0 : 
         return   0 
     if   x   <   10 : 
         return   x 
     l   =   len ( str ( x )) 
     return   f ( x   -   10   *   ( 10   **   ( l   -   2 )))   +   ( 10   **   ( l   -   1 ))   *   ( l   -   1 )   *   9   +   10   *   ( l   -   1 )

if __name__ == '__main__':
    ()