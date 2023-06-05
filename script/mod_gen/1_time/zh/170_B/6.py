def main():
    x,y = map(int,input().split())
    if y%2 == 0:
        if x <= y/2 and x >= y/4:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
main()
