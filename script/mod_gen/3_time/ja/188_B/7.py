def main():
    # 1行目
    n = int(input())
    # 2行目
    a = list(map(int, input().split()))
    # 3行目
    b = list(map(int, input().split()))
    
    # AとBの内積
    ab = 0
    for i in range(n):
        ab += a[i] * b[i]
    
    # 内積が0かどうか判定
    if ab == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()