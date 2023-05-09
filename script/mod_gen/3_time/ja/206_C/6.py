def main():
    n = int(input())
    a = list(map(int,input().split()))
    s = set(a)
    print(len(s)*(len(s)-1)//2)

if __name__ == '__main__':
    main()