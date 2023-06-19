def  solve ( N ,  A ,  B ):
    ans  =  [ [ 0  for  _  in  range ( B * N )]  for  _  in  range ( A * N )]
     for  i  in  range ( N ):
         for  j  in  range ( N ):
             for  k  in  range ( A ):
                 for  l  in  range ( B ):
                    ans [ A * i + k ][ B * j + l ] =  ( i + j + k + l )  %  2 
     for  i  in  range ( A * N ):
         for  j  in  range ( B * N ):
            ans [ i ][ j ] =  '.'   if  ans [ i ][ j ] ==  0   else  '#'
         print ( '' . join ( ans [ i ]))
