def main():
    N,A,B = map(int,input().split())
    q,r = divmod(N,A+B)
    print(q*A+min(r,A))

if __name__ == '__main__':
    main()