def  find_s ( s ,  n ):
     for  i  in  range ( n ):
         for  j  in  range ( n ):
             if  s [ i ][ j ] ==  ' # ' :
                 return  ( i ,  j )
     return  None
