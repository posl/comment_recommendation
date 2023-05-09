def main():
    n,m = map(int,input().split())
    s = list(map(str,input().split()))
    t = list(map(str,input().split()))
    for i in range(n):
        if s[i] in t:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()