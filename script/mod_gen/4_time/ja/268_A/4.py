def main():
    a,b,c,d,e = map(int,input().split())
    arr = [a,b,c,d,e]
    print(len(set(arr)))

if __name__ == '__main__':
    main()