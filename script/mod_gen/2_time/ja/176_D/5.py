def main():
    H,W = map(int,input().split())
    C_h,C_w = map(int,input().split())
    D_h,D_w = map(int,input().split())
    S = []
    for i in range(H):
        S.append(input())
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    ans = solve(H,W,C_h,C_w,D_h,D_w,S)
    print(ans)

if __name__ == '__main__':
    main()