def  main ():
    n  =  int ( input ())
    x  =  [ 0 ] * n
    y  =  [ 0 ] * n
    for  i  in  range (n):
        x[i], y[i]  =  map ( int , input (). split ())
    s  =  input ()
    for  i  in  range (n):
        if  s[i]  ==   'R' :
            for  j  in  range (n):
                if  s[j]  ==   'L'  and  x[i]  <  x[j]  and  y[i]  ==  y[j]:
                     print ( 'Yes' )
                     return 
        elif  s[i]  ==   'L' :
            for  j  in  range (n):
                if  s[j]  ==   'R'  and  x[i]  >  x[j]  and  y[i]  ==  y[j]:
                     print ( 'Yes' )
                     return 
     print ( 'No' )
