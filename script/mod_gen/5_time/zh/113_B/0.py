def main():
    n = int(input())
    t,a = map(int,input().split())
    h = list(map(int,input().split()))
    print(min(range(n),key=lambda i:abs(a-(t-h[i]*0.006)))+1)

if __name__ == '__main__':
    main()