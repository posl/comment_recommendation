def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    print("Yes" if A == list(range(1,N+1)) else "No")

if __name__ == '__main__':
    main()