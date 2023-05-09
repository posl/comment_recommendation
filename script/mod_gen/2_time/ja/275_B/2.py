def main():
    A,B,C,D,E,F = map(int,input().split())
    a = (A*B*C - D*E*F) % 998244353
    print(a)

if __name__ == '__main__':
    main()