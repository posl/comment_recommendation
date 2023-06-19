def   main ():
    n ,  m ,  q  =  map ( int ,  input (). split ())
    abcd  =  [ list ( map ( int ,  input (). split ()))  for  _  in   range ( q )]
    ans  =   0 
     for  a  in   range ( 1 ,  m  +   1 ):
        A  =   [ a ]  +   [ 0 ] * ( n  -   1 )
         for  i  in   range ( 1 ,  n ):
            A [ i ]  =   max ( A [ i - 1 ],  m  -  ( n  -  i ))
             if  A [ i ]  ==  m  -  ( n  -  i ):
                 break 
         for  b  in   range ( A [ i ],  m  +   1 ):
            A [ i ]  =  b
             for  j  in   range ( i + 1 ,  n ):
                A [ j ]  =   max ( A [ j - 1 ],  m  -  ( n  -  j ))
                 if  A [ j ]  ==  m  -  ( n  -  j ):
                     break 
             for  c  in   range ( A [ j ],  m  +   1 ):
                A [ j ]  =  c
                 for  k  in   range ( j + 1 ,  n ):
                    A [ k ]  =   max ( A [ k - 1 ],  m  -  ( n  -  k ))
                     if  A [ k ]  ==  m  -  ( n  -  k ):
                         break 
                 for  d  in   range ( A [ k ],  m  +   1 ):
                    A [ k ]  =  d
                    score  =   0 
                     for  a_i ,  b_i ,  c_i ,  d_i  in  abcd:
                         if  A [ b_i  -   1 ]  -  A [ a_i  -   1 ]  ==  c_i:
                            score  +=  d_i
                    ans  =   max ( ans ,  score )
    print ( ans )
