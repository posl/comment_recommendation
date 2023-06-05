def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    print(abs(P.index(1) - Q.index(1)))

if __name__ == '__main__':
    main()