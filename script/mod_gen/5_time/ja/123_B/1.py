def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    time = [a,b,c,d,e]
    time.sort()
    time.reverse()
    print(time[0])

if __name__ == '__main__':
    main()