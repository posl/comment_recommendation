def   solve ( N ,   K ,   H ): 
     H . sort () 
     min_diff   =   10 ** 9 
     for   i   in   range ( N   -   K   +   1 ): 
         min_diff   =   min ( min_diff ,   H [ i   +   K   -   1 ]   -   H [ i ]) 
     print ( min_diff )

if __name__ == '__main__':
    ()