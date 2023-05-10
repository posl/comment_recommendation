def main():
    h,w = map(int,input().split())
    H,W = map(int,input().split())
    print((h*w) - (H*w) - (h*W) + (H*W))
