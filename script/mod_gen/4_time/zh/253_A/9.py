def main():
    a,b,c = map(int,input().split())
    if b == max(a,b,c) or b == min(a,b,c):
        print("没有")
    else:
        print("是")

if __name__ == '__main__':
    main()