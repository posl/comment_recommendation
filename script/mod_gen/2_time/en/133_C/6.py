def   solve ( l ,   r ) : 
     if   r   -   l   >=   2019 : 
         return   0 
     else : 
         m   =   2019 
         for   i   in   range ( l ,   r ) : 
             for   j   in   range ( i   +   1 ,   r   +   1 ) : 
                 m   =   min ( m ,   ( i   *   j )   %   2019 ) 
         return   m

if __name__ == '__main__':
    ()