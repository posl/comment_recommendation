def main():
    x,k,d = map(int, input().split())
    x = abs(x)
    if x/k >= d:
        print(x-k*d)
    else:
        m = x//d
        x -= m*d
        k -= m
        if k % 2 == 0:
            print(x)
        else:
            print(abs(x-d))

if __name__ == '__main__':
    main()