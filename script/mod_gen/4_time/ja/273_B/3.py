def main():
    x,k = map(int,input().split())
    for i in range(k):
        if x % (10**(k-i)) < 5*(10**(k-i-1)):
            x = x - (x % (10**(k-i)))
        else:
            x = x + (10**(k-i)) - (x % (10**(k-i)))
    print(x)

if __name__ == '__main__':
    main()