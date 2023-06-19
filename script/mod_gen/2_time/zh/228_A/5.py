def main():
    s,t,x = map(int,input().split())
    if s > t:
        if x >= s or x <= t:
            print("Yes")
        else:
            print("No")
    else:
        if x >= s and x <= t:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()