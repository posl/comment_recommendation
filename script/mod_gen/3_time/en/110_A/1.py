def main():
    # Write your code here
    a, b, c = map(int, input().split())
    print(max(a*100+b*10+c, a*10+b+c*10, a*10+b+c, a+b*10+c*10, a+b*100+c*1, a+b*10+c*1))
main()

if __name__ == '__main__':
    main()