def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    l = [a,b,c,d,e]
    l.sort()
    for i in range(len(l)):
        if l[i]%10 == 0:
            continue
        else:
            l[i] = l[i] + (10 - (l[i]%10))
    print(sum(l)-10)
    return 0

if __name__ == '__main__':
    main()