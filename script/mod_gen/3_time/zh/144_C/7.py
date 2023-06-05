def main():
    n = int(input())
    x = int(n**0.5)
    if x*x == n:
        print(2*x-2)
    elif x*(x+1) >= n:
        print(2*x-1)
    else:
        print(2*x)

if __name__ == '__main__':
    main()