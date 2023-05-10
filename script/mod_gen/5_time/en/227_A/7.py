def main():
    n,k,a = map(int, input().split())
    if k <= (n-a):
        print(a+k)
    else:
        print(k-(n-a))

if __name__ == '__main__':
    main()