def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print(2*(H-1)*(W-1) - (H-1) - (W-1) + 1)
