def main():
    a,b = map(int,input().split())
    if a in [1,3,4,5,6,8,9,10,11,13,15] and b in [1,3,4,5,6,8,9,10,11,13,15]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()