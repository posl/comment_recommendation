def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    
    print(int(n/min(a,b,c,d,e)) + (5 if n%min(a,b,c,d,e) else 0) + 4)

if __name__ == '__main__':
    main()