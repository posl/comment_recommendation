def  main():
    n  =  int (input())
    x  =  [ 0 ] * n
    y  =  [ 0 ] * n
    for  i  in  range(n):
        x[i], y[i]  =  map( int , input().split())
    s  =  set ()
    for  i  in  range(n):
        for  j  in  range(n):
            if  i  ==  j:  continue 
            s.add((x[i] - x[j], y[i] - y[j]))
    print( len (s))

if __name__ == '__main__':
    ()