Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, K = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = 0
    for h in range(2**H):
        for w in range(2**W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if (h >> i) & 1 == 0 and (w >> j) & 1 == 0 and C[i][j] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]
    ans = 0
    for h in range(2**H):
        for w in range(2**W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if (h >> i) & 1 == 0 and (w >> j) & 1 == 0 and c[i][j] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    h, w, k = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(2 ** h):
        for j in range(2 ** w):
            cnt = 0
            for x in range(h):
                for y in range(w):
                    if i >> x & 1 or j >> y & 1:
                        continue
                    if c[x][y] == "#":
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    H, W, K = map(int, input().split())
    C = [input() for _ in range(H)]

    ans = 0
    for h in range(2 ** H):
        for w in range(2 ** W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if (h >> i & 1) == 0 and (w >> j & 1) == 0 and C[i][j] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1

    print(ans)

=======
Suggestion 5

def main():
    H, W, K = map(int, input().split())
    grid = [input() for _ in range(H)]
    ans = 0
    for i in range(1 << H):
        for j in range(1 << W):
            cnt = 0
            for h in range(H):
                for w in range(W):
                    if (i >> h) & 1 == 0 and (j >> w) & 1 == 0 and grid[h][w] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    H, W, K = map(int, input().split())
    C = [list(input()) for _ in range(H)]

    ans = 0
    for h in range(2 ** H):
        for w in range(2 ** W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if (h >> i) & 1 == 0 and (w >> j) & 1 == 0 and C[i][j] == "#":
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    H,W,K = map(int,input().split())
    C = [input() for i in range(H)]
    ans = 0
    for i in range(1 << H):
        for j in range(1 << W):
            count = 0
            for h in range(H):
                for w in range(W):
                    if (i >> h) & 1 == 1 and (j >> w) & 1 == 1 and C[h][w] == "#":
                        count += 1
            if count == K:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    from sys import stdin
    H, W, K = map(int, stdin.readline().split())
    C = [stdin.readline().rstrip() for _ in range(H)]
    ans = 0
    for h in range(2**H):
        for w in range(2**W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if (h >> i) & 1 == 0 and (w >> j) & 1 == 0 and C[i][j] == "#":
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 9

def  main():
    H, W, K = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            count = 0
            for h in range(H):
                for w in range(W):
                    if i >> h & 1 or j >> w & 1:
                        continue
                    if S[h][w] == "#":
                        count += 1
            if count == K:
                ans += 1
    print(ans)

=======
Suggestion 10

def  main():
     H ,  W ,  K  =  map( int ,  input().split())
     S  =  [ input()  for  _  in  range( H )]
     ans  =  0
     for  h  in  range( 1 <<  H ):
         for  w  in  range( 1 <<  W ):
            cnt  =  0
             for  i  in  range( H ):
                 for  j  in  range( W ):
                     if  h  &  ( 1  <<  i )  and  w  &  ( 1  <<  j ):
                         if  S[i][j]  ==  '#':
                            cnt  +=  1
            ans  +=  cnt  ==  K
