def main():
    x,k,d = map(int, input().split())
    x = abs(x)
    if x - k*d >= 0:
        print(x-k*d)
    else:
        if (x//d)%2 == k%2:
            print(x%d)
        else:
            print(d-x%d)

if __name__ == '__main__':
    main()