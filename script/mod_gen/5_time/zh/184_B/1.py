def main():
    n,x = map(int,input().split())
    s = input()
    count = x
    for i in s:
        if i == 'o':
            count += 1
        else:
            if count == 0:
                continue
            else:
                count -= 1
    print(count)

if __name__ == '__main__':
    main()