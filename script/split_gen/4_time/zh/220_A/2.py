def main():
    a,b,c = map(int,input().split())
    if a%c == 0:
        print(a)
    else:
        for i in range(a+1,b+1):
            if i%c == 0:
                print(i)
                break
            elif i == b:
                print(-1)
main()
