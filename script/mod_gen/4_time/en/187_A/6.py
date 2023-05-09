def main():
    a,b = input().split()
    sa = sum([int(i) for i in a])
    sb = sum([int(i) for i in b])
    print(max(sa,sb))

if __name__ == '__main__':
    main()