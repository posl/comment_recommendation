def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(360-min(A))

if __name__ == '__main__':
    main()