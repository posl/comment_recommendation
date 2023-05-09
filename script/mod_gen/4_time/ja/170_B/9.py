def main():
    x, y = map(int, input().split())
    # 鶴の数を i として全探索
    for i in range(x+1):
        # 鶴の数が決まれば亀の数も決まる
        j = x - i
        if 2*i + 4*j == y:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()