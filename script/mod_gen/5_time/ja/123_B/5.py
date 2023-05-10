def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    list = [a,b,c,d,e]
    list.sort()
    print(list[4] + (10 - list[4]%10) + list[3] + (10 - list[3]%10) + list[2] + (10 - list[2]%10) + list[1] + (10 - list[1]%10) + list[0] + (10 - list[0]%10))

if __name__ == '__main__':
    main()