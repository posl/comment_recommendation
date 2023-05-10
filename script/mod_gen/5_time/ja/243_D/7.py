def main():
    n,x = map(int,input().split())
    s = input()
    
    for i in range(n):
        if s[i] == "U":
            x = x//2
        elif s[i] == "L":
            x = x*2
        elif s[i] == "R":
            x = x*2+1
    print(x)

if __name__ == '__main__':
    main()