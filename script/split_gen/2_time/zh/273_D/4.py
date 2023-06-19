def main():
    h,w,r,c = map(int,input().split())
    n = int(input())
    wall = set()
    for i in range(n):
        r_i,c_i = map(int,input().split())
        wall.add((r_i,c_i))
    q = int(input())
    move = []
    for i in range(q):
        d_i,l_i = input().split()
        move.append((d_i,int(l_i)))
    ans = []
    #print(move)
    for i in range(q):
        d_i,l_i = move[i]
        #print(d_i,l_i)
        if d_i == 'L':
            for j in range(l_i):
                if (r,c-1) not in wall:
                    c -= 1
                else:
                    break
        elif d_i == 'R':
            for j in range(l_i):
                if (r,c+1) not in wall:
                    c += 1
                else:
                    break
        elif d_i == 'U':
            for j in range(l_i):
                if (r-1,c) not in wall:
                    r -= 1
                else:
                    break
        elif d_i == 'D':
            for j in range(l_i):
                if (r+1,c) not in wall:
                    r += 1
                else:
                    break
        ans.append((r,c))
    #print(ans)
    for i in range(q):
        print(ans[i][0],ans[i][1])
