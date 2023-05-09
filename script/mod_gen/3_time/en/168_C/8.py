def  main():
     A ,  B ,  H ,  M  =  map( int ,  input().split())
     h  =  H  *   60   +  M
     m  =  M
     d1  =  ( h  -  m )  *   360   /   720 
     d2  =   360   -  d1
     d  =  min(d1, d2)

if __name__ == '__main__':
    ()