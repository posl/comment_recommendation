def check():
    s,t,x = map(int,input().split())
    if s < t:
        if s <= x and x < t:
            print("Yes")
        else:
            print("No")
    else:
        if s <= x or x < t:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    check()