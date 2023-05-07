def   main (): 
     P   =   list ( map ( int ,   input (). split ())) 
     ans   =   "" 
     for   i   in   range ( 1 ,   27 ): 
         ans   +=   chr ( P . index ( i )   +   ord ( "a" )) 
     print ( ans )

if __name__ == '__main__':
    ()