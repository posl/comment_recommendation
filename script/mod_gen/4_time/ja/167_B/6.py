def main():
    a,b,c,k = map(int, input().split())
    print(min(a,k)-min(b,max(0,k-a)))

if __name__ == '__main__':
    main()