def   main (): 
     n   =   int ( input ()) 
     p   =   list ( map ( int ,   input (). split ())) 
     q   =   list ( map ( int ,   input (). split ())) 
     from   itertools   import   permutations 
     x   =   0 
     y   =   0 
     for   i ,   j   in   enumerate ( permutations ( range ( 1 ,   n   +   1 ))): 
         if   list ( j )   ==   p : 
             x   =   i 
         if   list ( j )   ==   q : 
             y   =   i 
     print ( abs ( x   -   y ))

if __name__ == '__main__':
    ()