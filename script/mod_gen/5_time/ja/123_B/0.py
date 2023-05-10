def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    
    time = 0
    
    if a % 10 != 0:
        time += a - (a % 10) + 10
    else:
        time += a
    time += b - (b % 10) + 10
    time += c - (c % 10) + 10
    time += d - (d % 10) + 10
    time += e - (e % 10) + 10
    
    print(time)

if __name__ == '__main__':
    main()