def   solve ( n ): 
     ans   =   0 
     for   i   in   range ( 1 ,   n   +   1 ): 
         if   n   %   i   ==   0 : 
             ans   +=   1 
     return   ans

if __name__ == '__main__':
    ()