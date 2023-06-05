def main():
    n,s,d = map(int, input().split())
    flag = False
    for i in range(n):
        x,y = map(int, input().split())
        if x < s and y > d:
            flag = True
    if flag:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()