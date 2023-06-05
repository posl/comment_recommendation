def main():
    h,m=map(int,input().split())
    if (h==0 and m==0) or (h==23 and m==59):
        print('0 0')
    elif m==59:
        print(h+1,'0')
    else:
        print(h,m+1)
