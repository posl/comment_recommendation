def  main():
    n, k = map( int , input().split())
    c = list(map( int , input().split()))
    d = set()
    for  i  in  range(n - k +  1 ):
        d.clear()
        for  j  in  range(i, i + k):
            d.add(c[j])
        if  len(d) == k:
             print ( k )
             return 
        elif  len(d) == 1:
             print ( 1 )
             return 
    print ( len(d) )
