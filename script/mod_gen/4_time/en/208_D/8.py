def  main():
    import  sys
    readline  =  sys.stdin.readline
    N, M  =   map ( int , readline().split())
    INF  =  10 **  6  *  400  +   1 
    G  =  [ [ INF  for  _  in   range (N)]  for  _  in   range (N)]
    for  _  in   range (M):
        A, B, C  =   map ( int , readline().split())
        G[A -  1 ][B -  1 ] = C
     for  k  in   range (N):
         for  i  in   range (N):
             for  j  in   range (N):
                G[i][j]  =   min (G[i][j], G[i][k] + G[k][j])
    ans  =   0 
     for  i  in   range (N):
         for  j  in   range (N):
             for  k  in   range (N):
                ans  +=   min (G[i][j], G[i][k] + G[k][j])
    print (ans)

if __name__ == '__main__':
    ()