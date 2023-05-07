def main():
    a,b = map(int,input().split())
    #h = 1
    #for i in range(1,a+1):
    #    h += i
    #h2 = 1
    #for i in range(1,b+1):
    #    h2 += i
    #print(h2-h)
    h = 0
    for i in range(1,a+1):
        h += i
    h2 = 0
    for i in range(1,b+1):
        h2 += i
    print(h2-h)

if __name__ == '__main__':
    main()