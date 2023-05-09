def main():
    x,k = map(int,input().split())
    for i in range(k):
        x = round(x,-i)
    print(x)

if __name__ == '__main__':
    main()