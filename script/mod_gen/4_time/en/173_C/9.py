def  main():
     H ,  W ,  K  =  map( int ,  input().split())
     S  =  [ input()  for  _  in  range( H )]
     ans  =  0
     for  h  in  range( 1 <<  H ):
         for  w  in  range( 1 <<  W ):
            cnt  =  0
             for  i  in  range( H ):
                 for  j  in  range( W ):
                     if  h  &  ( 1  <<  i )  and  w  &  ( 1  <<  j ):
                         if  S[i][j]  ==  '#':
                            cnt  +=  1
            ans  +=  cnt  ==  K

if __name__ == '__main__':
    ()