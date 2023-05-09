def  main():
    h, w, k =  map ( int , input().split())
    dp =  [ [ 0  for  _  in   range (w)]  for  _  in   range (h +  1 )]
    dp[ 0 ][ 0 ] =  1 
     for  i  in   range (h):
         for  j  in   range (w):
             if  j >  0 :
                dp[i +  1 ][j] += dp[i][j -  1 ]
             if  j < w -  1 :
                dp[i +  1 ][j] += dp[i][j +  1 ]
            dp[i +  1 ][j] %=  1000000007 
     print (dp[h][k -  1 ])

if __name__ == '__main__':
    ()