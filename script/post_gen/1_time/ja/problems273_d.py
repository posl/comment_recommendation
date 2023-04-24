Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    blocks = [tuple(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    instructions = [tuple(input().split()) for _ in range(Q)]

    blocks = set(blocks)

    for d, l in instructions:
        for _ in range(int(l)):
            if d == 'L':
                c_s -= 1
            elif d == 'R':
                c_s += 1
            elif d == 'U':
                r_s -= 1
            elif d == 'D':
                r_s += 1

            if (r_s, c_s) in blocks:
                if d == 'L':
                    c_s += 1
                elif d == 'R':
                    c_s -= 1
                elif d == 'U':
                    r_s += 1
                elif d == 'D':
                    r_s -= 1
                break

        print(r_s, c_s)

main()

=======
Suggestion 2

def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    block = set()
    for i in range(N):
        r_i, c_i = map(int, input().split())
        block.add((r_i, c_i))
    Q = int(input())
    for i in range(Q):
        d_i, l_i = input().split()
        l_i = int(l_i)
        if d_i == 'L':
            for j in range(l_i):
                if (r_s, c_s - 1) in block:
                    break
                else:
                    c_s -= 1
        if d_i == 'R':
            for j in range(l_i):
                if (r_s, c_s + 1) in block:
                    break
                else:
                    c_s += 1
        if d_i == 'U':
            for j in range(l_i):
                if (r_s - 1, c_s) in block:
                    break
                else:
                    r_s -= 1
        if d_i == 'D':
            for j in range(l_i):
                if (r_s + 1, c_s) in block:
                    break
                else:
                    r_s += 1
        print(r_s, c_s)

=======
Suggestion 3

def solve():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    block = set()
    for _ in range(N):
        r, c = map(int, input().split())
        block.add((r, c))
    Q = int(input())
    for _ in range(Q):
        d, l = input().split()
        l = int(l)
        for _ in range(l):
            if d == 'L' and (r_s, c_s - 1) not in block:
                c_s -= 1
            elif d == 'R' and (r_s, c_s + 1) not in block:
                c_s += 1
            elif d == 'U' and (r_s - 1, c_s) not in block:
                r_s -= 1
            elif d == 'D' and (r_s + 1, c_s) not in block:
                r_s += 1
        print(r_s, c_s)
solve()

=======
Suggestion 4

def solve():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    blocks = [tuple(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    directions = [input().split() for _ in range(Q)]

    blocks = set(blocks)
    blocks.add((r_s, c_s))
    for d, l in directions:
        if d == "L":
            for i in range(l):
                if (r_s, c_s - 1) not in blocks:
                    c_s -= 1
        elif d == "R":
            for i in range(l):
                if (r_s, c_s + 1) not in blocks:
                    c_s += 1
        elif d == "U":
            for i in range(l):
                if (r_s - 1, c_s) not in blocks:
                    r_s -= 1
        elif d == "D":
            for i in range(l):
                if (r_s + 1, c_s) not in blocks:
                    r_s += 1
        print(r_s, c_s)

solve()

=======
Suggestion 5

def solve():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    blocks = set()
    for i in range(N):
        r_i, c_i = map(int, input().split())
        blocks.add((r_i, c_i))
    Q = int(input())
    for i in range(Q):
        d_i, l_i = input().split()
        l_i = int(l_i)
        if d_i == "L":
            for j in range(l_i):
                if (r_s, c_s - 1) not in blocks:
                    c_s -= 1
        elif d_i == "R":
            for j in range(l_i):
                if (r_s, c_s + 1) not in blocks:
                    c_s += 1
        elif d_i == "U":
            for j in range(l_i):
                if (r_s - 1, c_s) not in blocks:
                    r_s -= 1
        elif d_i == "D":
            for j in range(l_i):
                if (r_s + 1, c_s) not in blocks:
                    r_s += 1
        print(r_s, c_s)

=======
Suggestion 6

def   main (): 
     # 入力を受け取る 
     H ,   W ,   r_s ,   c_s   =   map ( int ,   input (). split ()) 
     N   =   int ( input ()) 
     black   =   [] 
     for   _   in   range ( N ): 
         r_i ,   c_i   =   map ( int ,   input (). split ()) 
         black . append (( r_i ,   c_i )) 
     Q   =   int ( input ()) 
     LRUD   =   [] 
     for   _   in   range ( Q ): 
         d_i ,   l_i   =   input (). split () 
         LRUD . append (( d_i ,   int ( l_i ))) 

     # 高橋君の初期位置 
     r ,   c   =   r_s ,   c_s 

     # 各方向の壁までの距離 
     d   =   { 
         "L" :   c   -   1 , 
         "R" :   W   -   c , 
         "U" :   r   -   1 , 
         "D" :   H   -   r 
     } 

     # 各方向の壁までの距離を更新 
     for   d_i ,   l_i   in   LRUD : 
         d [ d_i ]   =   min ( d [ d_i ],   l_i ) 

     # 高橋君の移動 
     r   +=   d [ "D" ]   -   d [ "U" ] 
     c   +=   d [ "R" ]   -   d [ "L" ] 

     # 高橋君の移動後の位置を出力 
     print ( r ,   c ) 

     # 高橋君の移動後の位置を更新 
     r_s ,   c_s   =   r ,   c 

     # 各方向の壁までの距離を更新 
     for   d_i ,   l_i   in   LRUD : 
         d [ d_i ]   -=   l_i 

     # 高橋

=======
Suggestion 7

def   main (): 
     h ,   w ,   r_s ,   c_s   =   map ( int ,   input (). split ()) 
     n   =   int ( input ()) 
     r_c   =   [ tuple ( map ( int ,   input (). split ()))   for   _   in   range ( n )] 
     q   =   int ( input ()) 
     d_l   =   [ tuple ( input (). split ())   for   _   in   range ( q )] 

     r_c . sort () 

     for   r ,   c   in   r_c : 
         if   r   <   r_s   and   c   <   c_s : 
             r_s   -=   1 
         elif   r   <   r_s   and   c_s   <   c : 
             r_s   -=   1 
             c_s   +=   1 
         elif   r_s   <   r   and   c   <   c_s : 
             r_s   +=   1 
             c_s   -=   1 
         elif   r_s   <   r   and   c_s   <   c : 
             r_s   +=   1 
         elif   r   ==   r_s   and   c   <   c_s : 
             c_s   -=   1 
         elif   r   ==   r_s   and   c_s   <   c : 
             c_s   +=   1 
         elif   r   <   r_s   and   c   ==   c_s : 
             r_s   -=   1 
         elif   r_s   <   r   and   c   ==   c_s : 
             r_s   +=   1 

     for   d ,   l   in   d_l : 
         if   d   ==   'L' : 
             c_s   =   max ( c_s   -   l ,   1 ) 
         elif   d   ==   'R' : 
             c_s   =   min ( c_s   +   l ,   w ) 
         elif   d   ==   'U' : 
             r_s   =   max ( r_s   -   l ,   1 ) 
         elif   d   ==   'D' :

=======
Suggestion 8

def main():
    H, W, r, c = map(int, input().split())
    N = int(input())
    block = set()
    for i in range(N):
        r_i, c_i = map(int, input().split())
        block.add((r_i, c_i))
    Q = int(input())
    for i in range(Q):
        d, l = input().split()
        l = int(l)
        for j in range(l):
            if d == 'L':
                c -= 1
            elif d == 'R':
                c += 1
            elif d == 'U':
                r -= 1
            elif d == 'D':
                r += 1
            if (r, c) in block:
                if d == 'L':
                    c += 1
                elif d == 'R':
                    c -= 1
                elif d == 'U':
                    r += 1
                elif d == 'D':
                    r -= 1
                break
        print(r, c)

=======
Suggestion 9

def main():
    H, W, r, c = map(int, input().split())
    N = int(input())
    block = set()
    for i in range(N):
        r_i, c_i = map(int, input().split())
        block.add((r_i, c_i))
    Q = int(input())
    for i in range(Q):
        d, l = input().split()
        l = int(l)
        if d == 'L':
            for j in range(l):
                if (r, c - 1) not in block:
                    c -= 1
        elif d == 'R':
            for j in range(l):
                if (r, c + 1) not in block:
                    c += 1
        elif d == 'U':
            for j in range(l):
                if (r - 1, c) not in block:
                    r -= 1
        elif d == 'D':
            for j in range(l):
                if (r + 1, c) not in block:
                    r += 1
        print(r, c)

=======
Suggestion 10

def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    block = [[0, 0, 0, 0] for _ in range(N)]
    for i in range(N):
        r_i, c_i = map(int, input().split())
        block[i] = [r_i - 1, c_i - 1, r_i, c_i]
    Q = int(input())
    for _ in range(Q):
        d_i, l_i = input().split()
        l_i = int(l_i)
        if d_i == "L":
            c_s = max(c_s - l_i, 1)
        elif d_i == "R":
            c_s = min(c_s + l_i, W)
        elif d_i == "U":
            r_s = max(r_s - l_i, 1)
        elif d_i == "D":
            r_s = min(r_s + l_i, H)
        for i in range(N):
            if r_s == block[i][0] and c_s == block[i][1]:
                if d_i == "L":
                    c_s = min(c_s + l_i, W)
                elif d_i == "R":
                    c_s = max(c_s - l_i, 1)
                elif d_i == "U":
                    r_s = min(r_s + l_i, H)
                elif d_i == "D":
                    r_s = max(r_s - l_i, 1)
        print(r_s, c_s)
