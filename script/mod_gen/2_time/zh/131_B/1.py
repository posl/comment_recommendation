def main():
    n, l = map(int, input().split())
    if l >= 0:
        print(sum(range(l+1, l+n)))
    else:
        if n <= -l:
            print(sum(range(l+n, l)))
        else:
            print(sum(range(l+1, l+n)))

if __name__ == '__main__':
    main()