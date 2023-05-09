def main():
    A,B,C,K = map(int,input().split())
    print(min(A,K)-min(max(0,K-A-B),C))

if __name__ == '__main__':
    main()