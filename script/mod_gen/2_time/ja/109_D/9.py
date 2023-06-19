def  main ():
    h, w = map( int , input().split())
    a = [ list (map( int , input().split())) for  _  in  range (h)]
    ans = []
     for  i  in  range (h):
         for  j  in  range (w):
             if  a[i][j] % 2:
                a[i][j] -= 1
                 if  i < h - 1:
                    a[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
                 elif  j < w - 1:
                    a[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
    print ( len (ans))
     for  i  in  ans:
        print ( ' ' .join(map( str , i)))
