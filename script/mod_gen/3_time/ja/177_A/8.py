def main():
    #入力
    d,t,s = map(int,input().split())
    
    #計算
    if d/s <= t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()