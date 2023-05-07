def main():
    n,m,x,t,d = map(int, input().split())
    print(t + (n-x)*d if m > x else t + (m-1)*d)

if __name__ == '__main__':
    main()