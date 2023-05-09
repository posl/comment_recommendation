def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print((H-1)*W + (W-1)*H - (H-1)*(W-1))
