def main():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    print(4 if (r==1 or r==h) and (c==1 or c==w) else 3 if (r==1 or r==h) or (c==1 or c==w) else 2)
