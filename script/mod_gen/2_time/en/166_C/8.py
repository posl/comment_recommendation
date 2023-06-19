def  main():
     n ,  m  =  map ( int ,  input (). split ())
     h  =  list ( map ( int ,  input (). split ()))
     g  =  [ []  for  _  in  range ( n )]
     for  _  in  range ( m ):
         a ,  b  =  map ( int ,  input (). split ())
         g[ a  -  1 ]. append ( b  -  1 )
         g[ b  -  1 ]. append ( a  -  1 )
     ans  =  0 
     for  i  in  range ( n ):
         flag  =  True 
         for  j  in  g[ i ]:
             if  h[ i ] <= h[ j ]:
                 flag  =  False 
                 break 
         if  flag:
             ans  +=  1 
     print ( ans )
