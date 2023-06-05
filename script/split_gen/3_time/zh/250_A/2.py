def main():
    H, W = [int(i) for i in input().strip().split()]
    R, C = [int(i) for i in input().strip().split()]
    print((H-R+1)*(W-C+1))
