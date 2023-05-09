def   f ( n ): 
     if   n   <=   9 : 
         return   n 
     else : 
         length   =   len ( str ( n )) 
         ans   =   0 
         for   i   in   range ( 1 ,   length ): 
             ans   +=   9   *   10 ** ( i - 1 )   *   i 
         ans   +=   ( n   -   10 ** ( length - 1 )   +   1 )   *   length 
         return   ans

if __name__ == '__main__':
    ()