def main():
    A,B,N = map(int,input().split())
    ans = 0
    x = min(B-1,N)
    ans = max(ans,A*x//B-A*(x//B))
    print(ans)

if __name__ == '__main__':
    main()