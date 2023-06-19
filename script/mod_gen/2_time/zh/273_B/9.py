def main():
    x,k = map(int,input().split())
    for i in range(k):
        x = (x+5)//10*10
    print(x)

if __name__ == '__main__':
    main()