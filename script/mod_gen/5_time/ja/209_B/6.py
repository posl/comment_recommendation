def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    if total - N//2 <= X:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()