def main():
    x, k = map(int, input().split())
    #print(x, k)
    for i in range(1, k+1):
        y = round(x, -i)
        #print(y)
        x = y
    print(x)

if __name__ == '__main__':
    main()