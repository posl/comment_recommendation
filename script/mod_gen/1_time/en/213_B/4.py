def   main ():
    N  =  int ( input ())
    A  =  list ( map ( int ,  input (). split ()))
    A_min  =  min (A)
    A_max  =  max (A)
    A_min_index  =  A . index (A_min)
    A_max_index  =  A . index (A_max)
    if  A_min_index  <  A_max_index :
         print (A_max_index  +   1 )
    else :
         print (A_max_index  +   1 )

if __name__ == '__main__':
    ()