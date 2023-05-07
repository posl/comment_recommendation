def  lunlun ( n ) :
     if  n  <=   9 :
         return  [ str ( i )   for  i  in   range ( 1 , n + 1 ) ]
     else :
         return  [ str ( i )   for  i  in   range ( 1 , 10 ) ]  +  [ i + j  for  i  in  lunlun ( n // 10 )  for  j  in   [ str ( int ( i [ - 1 ] ) + k )   for  k  in   [ - 1 , 0 , 1 ]   if  0  <=  int ( i [ - 1 ] ) + k  < =   9 ]   if  i [ - 1 ]  !=   '0' ]  +  [ i + j  for  i  in  lunlun ( n // 10 + 1 )  for  j  in   [ str ( int ( i [ - 1 ] ) + k )   for  k  in   [ - 1 , 0 , 1 ]   if  0  <=  int ( i [ - 1 ] ) + k  < =   9 ]   if  i [ - 1 ]  !=   '0' ]

if __name__ == '__main__':
    ()