def main():
    p,q,r = map(int,input().split())
    print(min(p+q,r+p,r+q))

if __name__ == '__main__':
    main()