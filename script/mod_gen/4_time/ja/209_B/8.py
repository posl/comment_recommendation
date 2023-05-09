def main():
    N, X = map(int, input().split())
    A = map(int, input().split())
    if X >= sum(A) - N//2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()