def main():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print(H*W - (H-C)*W - (W-R)*H + (H-C)*(W-R))
