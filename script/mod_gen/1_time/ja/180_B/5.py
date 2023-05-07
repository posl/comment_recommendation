def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    X = list(map(int,input().split()))
    print(sum(map(abs,X)))
    print((sum(map(lambda x:x**2,X)))**0.5)
    print(max(map(abs,X)))

if __name__ == '__main__':
    main()