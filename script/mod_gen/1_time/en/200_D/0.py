def   main (): 
     N   =   int ( input ()) 
     A   =   list ( map ( int ,   input (). split ())) 
     mod200   =   [ []   for   _   in   range ( 200 )] 
     for   idx ,   a   in   enumerate ( A ): 
         mod200 [ a   %   200 ]. append ( idx + 1 ) 
     for   i   in   range ( 200 ): 
         if   len ( mod200 [ i ])   >=   2 : 
             print ( "Yes" ) 
             print ( len ( mod200 [ i ]),   * mod200 [ i ][: 2 ]) 
             print ( len ( mod200 [ i ]),   * mod200 [ i ][ 2 :]) 
             return 
     print ( "No" )

if __name__ == '__main__':
    ()