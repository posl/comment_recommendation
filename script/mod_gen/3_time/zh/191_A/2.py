def main():
    V,T,S,D = map(int,input().split())
    if T*V <= D and D <= S*V:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()