def   main (): 
     N   =   int ( input ()) 
     A   =   list ( map ( int ,   input (). split ())) 
     B   =   [] 
     C   =   [] 
     for   i   in   range ( N ): 
         if   A [ i ]   %   200   ==   0 : 
             B . append ( i   +   1 ) 
         else : 
             C . append ( i   +   1 ) 
     if   len ( B )   >   0   and   len ( C )   >   0   or   len ( B )   >=   2 : 
         print ( 'Yes' ) 
         if   len ( B )   >   0   and   len ( C )   >   0 : 
             print ( 1 ,   B [ 0 ]) 
             print ( 1 ,   C [ 0 ]) 
         else : 
             print ( 2 ,   B [ 0 ],   B [ 1 ]) 
             print ( 1 ,   C [ 0 ]) 
     else : 
         print ( 'No' )

if __name__ == '__main__':
    ()