def   main (): 
     X ,   N   =   map ( int ,   input (). split ()) 
     p   =   list ( map ( int ,   input (). split ())) 
     if   N   ==   0 : 
         print ( X ) 
         return 
     for   i   in   range ( 100 ): 
         if   X   -   i   not   in   p : 
             print ( X   -   i ) 
             return 
         if   X   +   i   not   in   p : 
             print ( X   +   i ) 
             return

if __name__ == '__main__':
    ()