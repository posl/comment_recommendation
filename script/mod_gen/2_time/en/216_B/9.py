def   main (): 
     n  =   int ( input ()) 
     names  =  [ input (). split ()   for   _   in   range ( n )] 
     names . sort () 
     for   i   in   range ( n - 1 ): 
         if   names [ i ][ 0 ] ==  names [ i + 1 ][ 0 ] and  names [ i ][ 1 ] ==  names [ i + 1 ][ 1 ]: 
             print ( 'Yes' ) 
             return 
     print ( 'No' )

if __name__ == '__main__':
    ()