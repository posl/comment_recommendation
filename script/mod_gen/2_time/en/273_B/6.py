def main():
    x, k = map(int, input().split())
    for i in range(k):
        if x % (10**(i+1)) <= 10**i:
            x = x - x % (10**(i+1))
        else:
            x = x - x % (10**(i+1)) + 10**(i+1)
    print(x)

if __name__ == '__main__':
    main()