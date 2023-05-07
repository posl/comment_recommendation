def main():
    a,b = map(int,input().split())
    for i in range(1,1001):
        if a == i*0.08 and b == i*0.1:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()