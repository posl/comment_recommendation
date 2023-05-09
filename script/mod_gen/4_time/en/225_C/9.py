def isMatched ( matrix ,  matrix2 ): 
     for  i  in   range ( len ( matrix )): 
         for  j  in   range ( len ( matrix [ i ])): 
             if  matrix [ i ][ j ] !=  matrix2 [ i ][ j ]: 
                 return   False 
     return   True 
 def  rotateMatrix ( matrix ): 
     return  [ list ( x )  for  x  in   zip ( * matrix [:: - 1 ])]
 def  main (): 
    N , M  =  map ( int , input (). split ()) 
    matrix  =   [ list ( map ( int , input (). split ()))  for  _  in   range ( N )] 
    matrix2  =   [ list ( map ( int , input (). split ()))  for  _  in   range ( N )] 
     if  isMatched ( matrix , matrix2 ): 
         print ( "Yes" ) 
         return 
     for  i  in   range ( 3 ): 
        matrix  =  rotateMatrix ( matrix ) 
         if  isMatched ( matrix , matrix2 ): 
             print ( "Yes" ) 
             return 
     print ( "No" ) 
 if   __name__  ==   '__main__' : 
    main ()

if __name__ == '__main__':
    isMatched()