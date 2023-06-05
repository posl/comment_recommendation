def main():
    v,t,s,d = map(int,input().split())
    if d < t * v or d > s * v:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()