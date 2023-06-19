def main():
    H,W = map(int,input().split())
    C_h,C_w = map(int,input().split())
    D_h,D_w = map(int,input().split())
    S = []
    for i in range(H):
        S.append(input())
    print(H,W,C_h,C_w,D_h,D_w)
    print(S)
