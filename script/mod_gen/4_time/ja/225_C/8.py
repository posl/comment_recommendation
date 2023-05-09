def main():
    n,m = map(int,input().split())
    b = [list(map(int,input().split())) for _ in range(n)]
    #print(b)
    if m == 1:
        if n == 1:
            print("Yes")
        else:
            print("No")
    else:
        if n == 1:
            print("Yes")
        else:
            if b[0][1] - b[0][0] == 1:
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    main()