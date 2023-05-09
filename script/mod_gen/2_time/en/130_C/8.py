def f(W,H,x,y):
    if x*2==W and y*2==H:
        return W*H/2,1
    else:
        return W*H/2,0
W,H,x,y=map(int,input().split())
print(*f(W,H,x,y))

if __name__ == '__main__':
    f()