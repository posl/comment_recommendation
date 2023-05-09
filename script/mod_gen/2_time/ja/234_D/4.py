def  main ( ) :
    N , K  =  map ( int , input ( ) . split ( ) )
    P  =  list ( map ( int , input ( ) . split ( ) ) )
    P  =  [ p - 1  for  p  in  P ]
    A  =  [ 0  for  _  in  range ( N ) ]
    for  i  in  range ( N ) :
        A [ P [ i ] ]  =  i
    #print(A)
     #A[i]:i+1が何番目か
    B  =  [ 0  for  _  in  range ( N ) ]
    B [ 0 ]  =  1
     #B[i]:i+1が何個あるか
    for  i  in  range ( N ) :
        B [ A [ i ] ]  +=  1
    #print(B)
     #B[i]:i+1が何個あるか
    C  =  [ 0  for  _  in  range ( N ) ]
    C [ 0 ]  =  1
     #C[i]:i+1が何個あるか
    for  i  in  range ( N ) :
        C [ B [ i ] ]  +=  1
    #print(C)
     #C[i]:i+1が何個あるか
    D  =  [ 0  for  _  in  range ( N ) ]
    D [ 0 ]  =  1
     #D[i]:i+1が何個あるか
    for  i  in  range ( N ) :
        D [ C [ i ] ]  +=  1
    #print(D)
     #D[i]:i+1が何個あるか
    E  =  [ 0  for  _  in  range ( N ) ]
    E [ 0 ]  =  1
     #E[i]:i+1が何個あるか
    for  i  in  range ( N ) :
        E [ D [ i ] ]  +=  1
    #print(E)
     #E[i]:i+1が

if __name__ == '__main__':
    ()