def   main (): 
     N   =   int ( input ()) 
     A   =   list ( map ( int ,   input (). split ())) 
     A   =   [ a   for   a   in   A   if   a   >   0 ] 
     N   =   len ( A ) 
     A   =   [ a   -   1   for   a   in   A ] 
     A   =   sorted ( A ) 
     A   =   [ a   +   1   for   a   in   A ] 
     A   =   [ a   -   1   for   a   in   A ] 
     # print(A) 
     # print(N) 
     #

if __name__ == '__main__':
    ()