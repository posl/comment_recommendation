def  solve():
    h, w, r_s, c_s =  map ( int , input().split())
    n =  int (input())
    walls = set()
    for  _  in  range (n):
        r, c =  map ( int , input().split())
        walls.add((r, c))
    q =  int (input())
    d = { 'L' :(- 1 ,  0 ),  'R' :( 1 ,  0 ),  'U' :( 0 ,  1 ),  'D' :( 0 , - 1 )}
    for  _  in  range (q):
        di, l = input().split()
        l =  int (l)
        for  _  in  range (l):
            r_s += d[di][ 0 ]
            c_s += d[di][ 1 ]
            if  (r_s, c_s)  in  walls:
                r_s -= d[di][ 0 ]
                c_s -= d[di][ 1 ]
        print(r_s, c_s)
