def   solve ( N ,   K ,   h ): 
     h . sort () 
     ans   =   10 ** 9 
     for   i   in   range ( N   -   K   +   1 ): 
         ans   =   min ( ans ,   h [ i   +   K   -   1 ]   -   h [ i ]) 
     return   ans

if __name__ == '__main__':
    ()