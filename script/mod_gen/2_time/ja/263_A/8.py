def main():
    #input
    a,b,c,d,e = map(int, input().split())
    #compute
    if(a==b==c and d==e):
        print('Yes')
    elif(a==b and c==d==e):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()