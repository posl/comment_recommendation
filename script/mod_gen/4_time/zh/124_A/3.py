def main():
    a,b = map(int, input().split())
    print(max(a+b, a+b-1, a*2-1, b*2-1))

if __name__ == '__main__':
    main()