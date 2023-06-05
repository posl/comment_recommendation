def main():
    A,B,N = map(int,input().split())
    # print(A,B,N)
    x = min(B-1,N)
    print((A*x)//B - A*(x//B))
    # print((A*x)//B - A*(x//B))
    # print((A*x)//B)
    # print(A*(x//B))

if __name__ == '__main__':
    main()