def permute ( a ,  b ):
    if  a  ==  b :
         return   1 
     else :
         return   0 
 def  main ():
    n  =   int ( input ())
    p  =  [ int (i)  for  i  in  input (). split ()]
    q  =  [ int (i)  for  i  in  input (). split ()]
    a  =   0 
    b  =   0 
     for  i  in   range (n):
        a  =  a  +  p [i] * 10 ** (n - i - 1 )
        b  =  b  +  q [i] * 10 ** (n - i - 1 )
     for  i  in   range (n):
        a  =  a  -  p [i] * 10 ** i
        b  =  b  -  q [i] * 10 ** i
        if  permute (a, b) ==  1 :
             print (i +  1 )
             break 
        a  =  a  +  p [i] * 10 ** i
        b  =  b  +  q [i] * 10 ** i
 if  __name__ ==  "__main__" :
    main ()

if __name__ == '__main__':
    permute()