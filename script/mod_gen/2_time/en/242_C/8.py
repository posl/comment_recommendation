def  main():
     N  =  int (input())
     dp  = [[ 0  for  _  in  range( 10 )] for  _  in  range( 2 )]
     for  i  in  range( 1 , 10 ):
        dp[ 0 ][i] =  1 
     for  i  in  range( 1 , N):
        for  j  in  range( 10 ):
             if  j ==  0 :
                dp[i %  2 ][j] = dp[(i -  1 ) %  2 ][j +  1 ]
                 continue 
             if  j ==  9 :
                dp[i %  2 ][j] = dp[(i -  1 ) %  2 ][j -  1 ]
                 continue 
            dp[i %  2 ][j] = dp[(i -  1 ) %  2 ][j -  1 ] + dp[(i -  1 ) %  2 ][j +  1 ]

if __name__ == '__main__':
    ()