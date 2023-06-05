def main():
    n,m,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    if x < a[-1] < b[0] and a[-1] < b[0] <= y:
        print("No War")
    else:
        print("War")

if __name__ == '__main__':
    main()