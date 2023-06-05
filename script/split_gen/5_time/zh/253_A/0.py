def main():
    a,b,c = map(int,input().split())
    if a <= b <= c:
        print("是")
    elif c <= b <= a:
        print("是")
    else:
        print("没有")
main()
