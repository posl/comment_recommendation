def main():
    A,B,N = map(int,input().split())
    if N < B-1:
        x = N
    else:
        x = B-1
    ans = (A*x)//B - A*(x//B)
    print(ans)

if __name__ == '__main__':
    main()