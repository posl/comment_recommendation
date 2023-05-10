def main():
    h,w = map(int,input().split())
    c_h,c_w = map(int,input().split())
    d_h,d_w = map(int,input().split())
    s = [input() for i in range(h)]
    c_h -= 1
    c_w -= 1
    d_h -= 1
    d_w -= 1
    q = [(c_h,c_w,0)]
    visited = {(c_h,c_w)}
    while q:
        c_h,c_w,c = q.pop(0)
        if c_h == d_h and c_w == d_w:
            print(c)
            return
        for i,j in [(c_h+1,c_w),(c_h-1,c_w),(c_h,c_w+1),(c_h,c_w-1)]:
            if 0<=i<h and 0<=j<w and s[i][j] == '.' and (i,j) not in visited:
                q.append((i,j,c))
                visited.add((i,j))
        for i in range(-2,3):
            for j in range(-2,3):
                if 0<=c_h+i<h and 0<=c_w+j<w and s[c_h+i][c_w+j] == '.' and (c_h+i,c_w+j) not in visited:
                    q.append((c_h+i,c_w+j,c+1))
                    visited.add((c_h+i,c_w+j))
    print(-1)
