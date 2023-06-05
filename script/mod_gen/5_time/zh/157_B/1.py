def bingo():
    a1,a2,a3 = map(int,input().split())
    b1,b2,b3 = map(int,input().split())
    c1,c2,c3 = map(int,input().split())
    N = int(input())
    b = [int(input()) for i in range(N)]
    if a1 in b and a2 in b and a3 in b or b1 in b and b2 in b and b3 in b or c1 in b and c2 in b and c3 in b or a1 in b and b1 in b and c1 in b or a2 in b and b2 in b and c2 in b or a3 in b and b3 in b and c3 in b or a1 in b and b2 in b and c3 in b or a3 in b and b2 in b and c1 in b:
        print("Yes")
    else:
        print("No")
bingo()
