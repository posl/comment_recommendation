def main():
    A,B,N = map(int,input().split())
    if B-1 <= N:
        x = B-1
    else:
        x = N
    print(A*x//B - A*(x//B))

if __name__ == '__main__':
    main()