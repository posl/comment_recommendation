def main():
    # Write your code here
    a,b,c = map(int, input().split())
    print(max(a+b, b+c, c+a))

if __name__ == '__main__':
    main()