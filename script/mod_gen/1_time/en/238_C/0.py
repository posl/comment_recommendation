def   main (): 
     N   =   int ( input ()) 
     mod   =   998244353 
     ans   =   0 
     for   i   in   range ( len ( str ( N ))): 
         ans   +=   ( N   -   10   **   i   +   1 )   *   ( 10   **   i )   %   mod 
         ans   %=   mod 
     print ( ans )

if __name__ == '__main__':
    ()