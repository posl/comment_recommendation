def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print((H-1)*(W-1) + (H-1)+(W-1) - 2*min(R-1, H-R) - 2*min(C-1, W-C))
