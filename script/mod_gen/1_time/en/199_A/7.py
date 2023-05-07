def main():
    #read input
    a,b,c = map(int,input().split())
    #compare a^2 + b^2 < c^2
    if a**2 + b**2 < c**2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()