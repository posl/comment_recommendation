def main():
    n,m,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(x+1,y+1):
        if max(a) < i and min(b) >= i:
            print('No War')
            exit()
    print('War')
    return
