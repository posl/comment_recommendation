def main():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    print((h-1)*w + (w-1)*h - (h-1)*(w-1))
